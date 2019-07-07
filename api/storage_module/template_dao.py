#!/usr/bin/python3
from storage_module.mongodb import MongoDB

class TemplateDao:

    #constructor
    def __init__(self):
        self.db = MongoDB()
        self.db.connect()

    def getTemplatesType(self, filter={}):
        return self.db.searchDocuments('template_type', filter)

    def getTemplateType(self, filter={}):
        return self.db.searchDocument('template_type', filter)

    def addTemplateType(self, document):
        self.db.addDocument('template_type', document)

    def getTemplatesMeta(self, filter={}):
        return self.db.searchDocuments('template_meta', filter)

    def getTemplateMeta(self, filter={}):
        return self.db.searchDocument('template_meta', filter)

    def addTemplateMeta(self, document):
        self.db.addDocument('template_meta', document)

    def getTemplatesSession(self, filter={}):
        return self.db.searchDocuments('template_session', filter)

    def getTemplateSession(self, filter={}):
        return self.db.searchDocument('template_session', filter)
        
    def addTemplateSession(self, document):
        self.db.addDocument('template_session', document)