#!/usr/bin/python3
from storage_module.mongodb import MongoDB

class TemplateDao:

    #constructor
    def __init__(self):
        self.db = MongoDB()
        self.db.connect()

    def removeTemplate(self, filter):
        """
        Removes all documents related with the template type identifier by a key
        """
        collections=['template_type','template_meta','template_session']
        return self.db.deleteCascadeDocuments(collections, filter)

    def getTemplatesType(self, filter={}):
        return self.db.searchDocuments('template_type', filter)

    def getTemplateType(self, filter={}):
        return self.db.searchDocument('template_type', filter)

    def addTemplateType(self, document):
        return self.db.addDocument('template_type', document)

    def updateTemplateType(self, document, filter):
        return self.db.updateDocument('template_type', filter, document)

    def removeTemplateType(self, filter):
        """
        Removes template type is not allowed.
        Use the removeTemplate to remove all documents related with the survey template
        """
        # return self.db.deleteDocument('template_type', filter)
        return False

    def getTemplatesMeta(self, filter={}):
        return self.db.searchDocuments('template_meta', filter)

    def getTemplateMeta(self, filter={}):
        return self.db.searchDocument('template_meta', filter)

    def addTemplateMeta(self, document):
        return self.db.addDocument('template_meta', document)

    def updateTemplateMeta(self, document, filter):
        return self.db.updateDocument('template_meta', filter, document)

    def removeTemplateMeta(self, filter):
        """
        Removes template meta is not allowed.
        Use the removeTemplate to remove all documents related with the survey template
        """
        # return self.db.deleteDocument('template_meta', filter)
        return False

    def getTemplatesSession(self, filter={}):
        return self.db.searchDocuments('template_session', filter)

    def getTemplateSession(self, filter={}):
        return self.db.searchDocument('template_session', filter)
        
    def addTemplateSession(self, document):
        return self.db.addDocument('template_session', document)

    def updateTemplateSession(self, document, filter):
        return self.db.updateDocument('template_session', filter, document)

    def removeTemplateSession(self, filter):
        """
        Removes template session is not allowed.
        Use the removeTemplate to remove all documents related with the survey template
        """
        # return self.db.deleteDocument('template_session', filter)
        return False
        