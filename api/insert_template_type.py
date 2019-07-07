from storage_module.template_dao import TemplateDao
import json

dao = TemplateDao()

document="""{"key":"default", "name":"Formulário Caieiras"}"""
jsonDoc=json.loads(document)
dao.addTemplateType(jsonDoc)

document="""{"key":"landslide", "name":"Risco de escorregamento"}"""
jsonDoc=json.loads(document)
dao.addTemplateType(jsonDoc)