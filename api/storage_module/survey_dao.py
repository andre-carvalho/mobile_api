#!/usr/bin/python3
from storage_module.mongodb import MongoDB

class SurveyDao:

    #constructor
    def __init__(self):
        self.db = MongoDB()
        self.db.connect()

    def getSurveys(self, filter={}):
        return self.db.searchDocuments('survey', filter)

    def getSurvey(self, filter={}):
        return self.db.searchDocument('survey', filter)
        
    def addSurvey(self, document):
        self.db.addDocument('survey', document)

    def getMetas(self, filter={}):
        return self.db.searchDocuments('meta', filter)

    def getMeta(self, filter={}):
        return self.db.searchDocument('meta', filter)
        
    def addMeta(self, document):
        self.db.addDocument('meta', document)