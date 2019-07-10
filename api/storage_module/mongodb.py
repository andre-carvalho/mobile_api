from pymongo import MongoClient, Cli
from storage_module.configdb import ConfigDB
from storage_module.app_exceptions import ConnectionError, QueryError
import urllib

class MongoDB:
    
    def __init__(self):
        # read connection parameters
        try:
            conf = ConfigDB('mongo.cfg','mongodb')
            self.params = conf.get()
        except Exception as configError:
            raise configError

    def connect(self):
        self.client = None
        self.db = None
        try:
            strConnection="mongodb://" + self.params['username'] + ":" + urllib.parse.quote(self.params['password'])  + "@" + self.params['host'] + ":" + self.params['port'] + '/?authSource=admin'
            # connect to the MongoDB server
            self.client = MongoClient(strConnection)
            # select or create a database
            self.db = self.client[self.params['database']]
        except (Exception) as error:
            raise ConnectionError('Missing connection:', error)
    
    def addDocument(self, collection, document):
        """
        Add one document to a collection.
        If the document have an _id parameter it is used otherwise one is auto generated.
        """
        # select a collection
        aCollection=self.db[collection]
        doc_id=aCollection.insert_one(document)
        return doc_id

    def updateDocument(self, collection, query, document):
        """
        Update one document into one collection using a query statement and a document or fragment of document.
        Return the integer one (1) if the document was found and updated.
        """
        # select a collection
        aCollection=self.db[collection]
        result=aCollection.update_one(query, {'$set':document})
        return result.modified_count
    
    def searchDocument(self, collection, query={}):
        """
        Retrieve one document from one collection using a query statement or not.
        """
        aCollection=self.db[collection]
        doc=aCollection.find_one(query, {"_id": 0})
        return doc

    def searchDocuments(self, collection, query={}):
        """
        Retrieve a list of documents from one collection using a query statement or not.
        """
        aCollection=self.db[collection]
        # set the option {"_id": 0} to hide the ObjectId used by internal control of the Mongo.
        doc=list(aCollection.find(query,{"_id": 0}))
        return doc
    
    def deleteDocument(self, collection, query):
        """
        Delete one document from one collection using a query statement.
        Return the integer one (1) if the document was found and removed.
        """
        # select a collection
        aCollection=self.db[collection]
        result=aCollection.delete_one(query)
        return result.deleted_count

    def deleteCascadeDocuments(self, collections, query):
        """
        Drop documents into a list of collections using transaction.
        The collections expect a list of collection names. collections=['coll_a','coll_b','coll_c']
        """
        try:
        
            for collection in collections:
                dbCollections[collection]=self.db[collection]

            with self.client.start_session() as session:
                with session.start_transaction():
                    for dbCollection in dbCollections:
                        dbCollection.delete_one(query, session=session)
                session.end_session()
            
            return True
        except Exception as error:
            return False
    
    def countDocuments(self, collection, query):
        """
        Count the number of documents in the collection.
        """
        # select a collection
        aCollection=self.db[collection]
        return aCollection.count_documents(query)
