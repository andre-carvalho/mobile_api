from storage_module.template_dao import TemplateDao
from storage_module.survey_dao import SurveyDao
import json

class TemplateService:

    def __init__(self):
        self.tpl_dao=TemplateDao()
        self.survey_dao=SurveyDao()

    def __prepareResponseList(templates):
        if len(templates)>0:
            jsonTemplates=""
            for template in templates:
                jsonTemplates+=( "" if jsonTemplates=="" else "," )+json.dumps(template)
            jsonTemplates="["+jsonTemplates+"]"
            return jsonTemplates
        else:
            return False

    def __add(template, option):
        jsonDoc=json.loads(template)
        if option=='type':
            doc_id=self.tpl_dao.addTemplateType(jsonDoc)
        elif option=='meta':
            doc_id=self.tpl_dao.addTemplateMeta(jsonDoc)
        elif option=='session':
            doc_id=self.tpl_dao.addTemplateSession(jsonDoc)
        if doc_id:
            return True
        else:
            return False

    def __update(key, template, option):
        jsonDoc=json.loads(template)
        if option=='type':
            count=self.tpl_dao.updateTemplateType(jsonDoc, {'key': key})
        elif option=='meta':
            count=self.tpl_dao.updateTemplateMeta(jsonDoc, {'key': key})
        elif option=='session':
            count=self.tpl_dao.updateTemplateSession(jsonDoc, {'key': key})
        if count==1:
            return True
        else:
            return False

    def removeTemplateByKey(self, key):
        count=self.survey_dao.countMeta({'surveyType': key})
        if count>0:
            # if exists one or more forms based in that template, the remotion is deny
            return False
        else:
            return self.tpl_dao.removeTemplate({'key': key})

    def getAllTypes(self):
        templates=self.tpl_dao.getTemplatesType()
        return self.__prepareResponseList(templates)

    def getAllMetas(self):
        templates=self.tpl_dao.getTemplatesMeta()
        return self.__prepareResponseList(templates)

    def getAllSessions(self):
        templates=self.tpl_dao.getTemplatesSession()
        return self.__prepareResponseList(templates)
    
    def addType(self, template):
        return self.__add(template, 'type')

    def addMeta(self, template):
        return self.__add(template, 'meta')

    def addSession(self, template):
        return self.__add(template, 'session')

    def getTemplateTypeByKey(self, key):
        template=self.tpl_dao.getTemplateType({'key': key})
        return json.dumps(template)

    def getTemplateMetaByKey(self, key):
        template=self.tpl_dao.getTemplateMeta({'key': key})
        return json.dumps(template)

    def getTemplateSessionByKey(self, key):
        template=self.tpl_dao.getTemplateSession({'key': key})
        return json.dumps(template)

    def updateTemplateTypeByKey(self, key, template):
        return self.__update(key, template, 'type')

    def updateTemplateMetaByKey(self, key, template):
        return self.__update(key, template, 'meta')

    def updateTemplateSessionByKey(self, key, template):
        return self.__update(key, template, 'session')