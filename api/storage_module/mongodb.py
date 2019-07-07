from pymongo import MongoClient
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
        self.conn = None
        self.collection = None
        try:
            strConnection="mongodb://" + self.params['username'] + ":" + urllib.parse.quote(self.params['password'])  + "@" + self.params['host'] + ":" + self.params['port'] + '/?authSource=admin'
            # connect to the MongoDB server
            self.conn = MongoClient(strConnection)
            # select or create a database
            self.collection = self.conn[self.params['database']]
        except (Exception) as error:
            raise ConnectionError('Missing connection:', error)
    
    def addDocument(self, collection, document):
        """
        Add one document to a collection.
        If the document have an _id parameter it is used otherwise one is auto generated.
        """
        # select a collection
        aCollection=self.collection[collection]
        doc_id=aCollection.insert_one(document)
        return doc_id

    def updateDocument(self, collection, query, document):
        """
        Update one document into one collection using a query statement and a document or fragment of document.
        """
        # select a collection
        aCollection=self.collection[collection]
        aCollection.update_one(query, {'$set':document})
    
    def searchDocument(self, collection, query={}):
        """
        Retrieve one document from one collection using a query statement or not.
        """
        aCollection=self.collection[collection]
        doc=aCollection.find_one(query, {"_id": 0})
        return doc

    def searchDocuments(self, collection, query={}):
        """
        Retrieve a list of documents from one collection using a query statement or not.
        """
        aCollection=self.collection[collection]
        doc=list(aCollection.find(query,{"_id": 0}))
        return doc
    
    def deleteDocument(self, collection, query):
        """
        Delete one document from one collection using a query statement.
        """
        # select a collection
        aCollection=self.collection[collection]
        aCollection.delete_one(query)