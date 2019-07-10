#!/usr/bin/python3
from storage_module.mongodb import MongoDB

class SurveyDao:

    #constructor
    def __init__(self):
        self.db = MongoDB()
        self.db.connect()

    def countSurvey(self, filter={}):
        return self.db.countDocuments('survey', filter)

    def countMeta(self, filter={}):
        return self.db.countDocuments('meta', filter)

    def getSurveys(self, filter={}):
        return self.db.searchDocuments('survey', filter)

    def getSurvey(self, filter={}):
        return self.db.searchDocument('survey', filter)
        
    def addSurvey(self, document):
        return self.db.addDocument('survey', document)

    def delSurvey(self, filter):
        return self.db.deleteDocument('survey', filter)

    def updateSurvey(self, filter, document):
        return self.db.updateDocument('survey', filter, document)

    def getMetas(self, filter={}):
        return self.db.searchDocuments('meta', filter)

    def getMeta(self, filter={}):
        return self.db.searchDocument('meta', filter)
        
    def addMeta(self, document):
        return self.db.addDocument('meta', document)

    def delMeta(self, filter):
        return self.db.deleteDocument('meta', filter)

    def updateMeta(self, filter, document):
        return self.db.updateDocument('meta', filter, document)