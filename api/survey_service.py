from storage_module.survey_dao import SurveyDao
import json

class SurveyService:

    def __init__(self):
        self.dao=SurveyDao()

    def __removeSurveyMetaByKey(self, survey_key):
        count=self.dao.delMeta({"key":survey_key})
        if count==1:
            return True
        else:
            return False
    
    def __removeSurveyMetaByDocId(self, doc_id):
        count=self.dao.delMeta({"_id":doc_id})
        if count==1:
            return True
        else:
            return False

    def searchByTerms(self, start_date, end_date, status, type=None, custom=None, code=None):
        filter={
            "date": {
                "$gte": ISODate(start_date),
                "$lte": ISODate(end_date)
            },
            "status": status
        }
        if type:
            filter.update({"surveyType":type})
        # if custom:
        #     filter.update({"surveyType":custom})

        # the code is one key or fragment of one key so, we will find using the "like" filter
        if code:
            filter.update({"key":{"$regex":"/"+code+"/"}})
        
        metas=self.dao.getMetas(filter)
        return json.dumps(metas)

    def getAllSurveyMeta(self):
        surveyMetas=self.dao.getMetas()
        return json.dumps(surveyMetas)

    def getSurveyMetaByKey(self, survey_key):
        aSurveyMeta=self.dao.getMeta({"key":survey_key})
        return json.dumps(aSurveyMeta)

    def addSurveyMeta(self, document):
        jsonDoc=json.loads(document)
        # mark as remote origin
        jsonDoc['origin']='remote'
        doc_id=self.dao.addMeta(jsonDoc)
        return doc_id

    def updateSurveyMetaByKey(self, survey_key, document):
        jsonDoc=json.loads(document)
        count=self.dao.updateMeta({"key":survey_key}, jsonDoc)
        if count==1:
            return True
        else:
            return False

    def getAllSurvey(self):
        surveys=self.dao.getSurveys()
        return json.dumps(surveys)

    def getSurveyByKey(self, survey_key):
        aSurvey=self.dao.getSurvey({"key":survey_key})
        return json.dumps(aSurvey)

    def removeSurveyByKey(self, survey_key):
        aMeta=self.getSurveyMetaByKey(survey_key)
        count=self.__removeSurveyMetaByKey({"key":survey_key})
        if count==1:
            count=self.dao.delSurvey({"key":survey_key})
            if count==1:
                return True
            else:
                self.addSurveyMeta(aMeta)
                return False
        else:
            return False

    def addSurvey(self, document):
        jsonDoc=json.loads(document)
        doc_id=self.dao.addSurvey(jsonDoc)
        return doc_id

    def updateSurveyByKey(self, survey_key, document):
        count=self.dao.updateSurvey({"key":survey_key}, document)
        if count==1:
            return True
        else:
            return False
    
    # Store the Survey and the Meta in the same time
    def addSurveyAndMeta(self, survey, meta):
        resultMeta=self.addSurveyMeta(meta)
        if resultMeta:
            resultSurvey=self.addSurvey(survey)
            if resultSurvey:
                return True
            else:
                self.__removeSurveyMetaByDocId(resultMeta)
                return False
        else:
            return False