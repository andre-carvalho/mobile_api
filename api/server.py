import os
import json
from flask import Flask, request, send_from_directory
from flask_restful import abort, Api, Resource
from werkzeug.utils import secure_filename
from flask_cors import CORS
#from storage_module.midias_dao import MidiasDao
from logs_module.log_writer import logWriter
from survey_service import SurveyService
from template_service import TemplateService

UPLOAD_FOLDER = '/tmp/uploadImages'
ALLOWED_EXTENSIONS = set(['png', 'jpg'])

SERVER_IP='0.0.0.0'
LOG_PATH='/logs'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

class Photo(Resource):
    
    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
    def post(self):
        # check if the post request has the file part
        if 'data' not in request.files or 'form_id' not in request.form:
            # No file part
            error_msg = 'Error in Photo class when trying test the file part from request. Return HTTP:500'
            logWriter(os.path.abspath(os.curdir) + LOG_PATH).write(error_msg)
            return {'status': 'parse error'}, 500
        file = request.files['data']
        form_id = request.form['form_id']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '' or form_id == '':
            error_msg = 'Error in Photo class when trying read the filename. Return HTTP:500'
            logWriter(os.path.abspath(os.curdir) + LOG_PATH).write(error_msg)
            return {'status': 'parse error'}, 500
        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if not os.path.isdir(app.config['UPLOAD_FOLDER'] + '/' +form_id):
                os.mkdir(app.config['UPLOAD_FOLDER'] + '/' +form_id)
            file.save(os.path.join(app.config['UPLOAD_FOLDER']+ '/' +form_id, filename))
            return {'status':'completed'}, 201

    def get(self, form_id, photo_id):
        dir=os.path.join(app.config['UPLOAD_FOLDER'],form_id)
        filename=photo_id+'.jpg'
        # trying read picture from disk and send to client
        try:
            if os.path.isfile(dir+'/'+filename):
                return send_from_directory(dir, filename, as_attachment=False)
            else:
                abort(404)
        except Exception as error:
            error_msg = 'Error in Photo class when trying load picture({0}) from disk. Return HTTP:404'.format(photo_id)
            logWriter(os.path.abspath(os.curdir) + LOG_PATH).write(error_msg)
            error_msg = str(error)
            logWriter(os.path.abspath(os.curdir) + LOG_PATH).write(error_msg)
            return 404


class SurveyMetaList(Resource):

    def __init__(self):
        self.surveyService=SurveyService()
    
    def get(self):
        """
        Return all survey metadata that match with default filter stored in the server.
        The default filter is used to provide a response time and a size package acceptable to use by an App.
        TODO: implement the default filter.
        """
        allMetas=self.surveyService.getAllSurveyMeta()
        return allMetas, 200

class SurveyMeta(Resource):

    def __init__(self):
        self.surveyService=SurveyService()

    def get(self, survey_key):
        """
        Delivery one metadata survey filtered by a key.
        """
        aSurveyMeta=self.surveyService.getSurveyMetaByKey(survey_key)
        return aSurveyMeta, 200

    def delete(self, survey_key):
        """
        Removes the metadata of survey is not allowed.
        When remove one Survey the metadata will be removed too.
        """
        if self.surveyService.removeSurveyByKey(survey_key)==1:
            return {'status':'ok'}, 200
        else:
            return {'status':'no found'}, 404

    def put(self, survey_key):
        args = parser.parse_args()
        document=json.loads(args['meta'])
        if self.surveyService.updateSurveyMetaByKey(survey_key, document)==1:
            return {'status':'ok'}, 200
        else:
            return {'status':'no found'}, 404

class SurveyList(Resource):

    def __init__(self):
        self.surveyService=SurveyService()
    
    def get(self):
        """
        Return all survey stored in the server
        Use some restriction if the number of stored surveys is big...
        """
        allSurveys=self.surveyService.getAllSurvey()
        return allSurveys, 200

    def post(self):
        """
        Receive a survey composed by survey bady and a survey meta and store in the server
        """
        # check if the post request has the survey document and survey meta
        if 'survey_document' not in request.form or 'survey_meta' not in request.form:
            # No survey_document or survey_meta
            error_msg = 'Error in SurveyList class when trying test the survey_document and survey_meta from request. Return HTTP:500'
            logWriter(os.path.abspath(os.curdir) + LOG_PATH).write(error_msg)
            return {'status': 'parse error'}, 500
        survey_document = request.form['survey_document']
        survey_meta = request.form['survey_meta']
        if survey_document == '' or survey_meta == '':
            error_msg = 'Error in SurveyList class when trying read the survey_document and survey_meta. Return HTTP:500'
            logWriter(os.path.abspath(os.curdir) + LOG_PATH).write(error_msg)
            return {'status': 'missing document'}, 500
        if self.surveyService.addSurveyAndMeta(survey_document, survey_meta):
            return {'status':'ok'}, 200
        else:
            return {'status': 'store error'}, 500

class Survey(Resource):

    def __init__(self):
        self.surveyService=SurveyService()
    
    def get(self, survey_key):
        aSurvey=self.surveyService.getSurveyByKey(survey_key)
        return aSurvey, 200

    def delete(self, survey_key):
        """
        When remove one survey the survey meta will be remove too.
        """
        if self.surveyService.removeSurveyByKey(survey_key)==1:
            return {'status':'ok'}, 200
        else:
            return {'status':'no found'}, 404

    def put(self, survey_key):
        args = parser.parse_args()
        document=json.loads(args['survey'])
        if self.surveyService.updateSurveyByKey(survey_key, document)==1:
            return {'status':'ok'}, 200
        else:
            return {'status':'no found'}, 404

class SurveySearch(Resource):

    def __init__(self):
        self.surveyService=SurveyService()

    def get(self, start_date, end_date, status, type=None, custom=None, code=None):
        surveys=self.surveyService.searchByTerms(start_date, end_date, status, type, custom, code)
        return surveys, 200


# Template classes
class TemplateTypeList(Resource):

    def __init__(self):
        self.templateService=TemplateService()

    def get(self):
        """
        Return all templates types of survey stored in the server
        """
        templates=self.templateService.getAllTypes()
        if templates==False:
            return {'status':'no found'}, 404
        else:
            return templates, 200

    def post(self):
        """
        Receive a survey template and store in the server
        """
        # check if the post request has the survey template document
        if 'template_type' not in request.form:
            # No template_type
            error_msg = 'Error in TemplateTypeList class when trying test the template_type from request. Return HTTP:500'
            logWriter(os.path.abspath(os.curdir) + LOG_PATH).write(error_msg)
            return {'status': 'parse error'}, 500
        template_type = request.form['template_type']
        if template_type == '':
            error_msg = 'Error in TemplateTypeList class when trying read the template_type. Return HTTP:500'
            logWriter(os.path.abspath(os.curdir) + LOG_PATH).write(error_msg)
            return {'status': 'missing document'}, 500
        if self.templateService.addType(template_type):
            return {'status':'ok'}, 200
        else:
            return {'status': 'store error'}, 500

class TemplateType(Resource):

    def __init__(self):
        self.templateService=TemplateService()
    
    def get(self, tpl_key):
        aTplType=self.templateService.getTemplateTypeByKey(tpl_key)
        return aTplType, 200

    def delete(self, tpl_key):
        """
        When remove one survey type the related survey templates will be remove too.
        It's allowed only if no forms uses the template.
        """
        if self.templateService.removeTemplateByKey(tpl_key)==1:
            return {'status':'ok'}, 200
        else:
            return {'status':'no found'}, 404

    def put(self, tpl_key):
        """
        The update of template type is disallowed to the key, only to the other properties.
        """
        args = parser.parse_args()
        document=json.loads(args['template_type'])
        document['key']=tpl_key
        if self.templateService.updateTemplateTypeByKey(tpl_key, document)==1:
            return {'status':'ok'}, 200
        else:
            return {'status':'no found'}, 404


class TemplateMetaList(Resource):

    def __init__(self):
        self.templateService=TemplateService()

    def get(self):
        """
        Return all templates meta of survey stored in the server
        """
        templates=self.templateService.getAllMetas()
        if templates==False:
            return {'status':'no found'}, 404
        else:
            return templates, 200

    def post(self):
        """
        Receive a survey template and store in the server
        """
        # check if the post request has the survey template document
        if 'template_meta' not in request.form:
            # No template_meta
            error_msg = 'Error in TemplateTypeList class when trying test the template_meta from request. Return HTTP:500'
            logWriter(os.path.abspath(os.curdir) + LOG_PATH).write(error_msg)
            return {'status': 'parse error'}, 500
        template_meta = request.form['template_meta']
        if template_meta == '':
            error_msg = 'Error in TemplateTypeList class when trying read the template_meta. Return HTTP:500'
            logWriter(os.path.abspath(os.curdir) + LOG_PATH).write(error_msg)
            return {'status': 'missing document'}, 500
        if self.templateService.addMeta(template_meta):
            return {'status':'ok'}, 200
        else:
            return {'status': 'store error'}, 500


class TemplateMeta(Resource):

    def __init__(self):
        self.templateService=TemplateService()
    
    def get(self, tpl_key):
        aTplMeta=self.templateService.getTemplateMetaByKey(tpl_key)
        return aTplMeta, 200

    def delete(self, tpl_key):
        """
        When remove one survey meta the related survey templates will be remove too.
        It's allowed only if no forms uses the template.
        """
        if self.templateService.removeTemplateByKey(tpl_key)==1:
            return {'status':'ok'}, 200
        else:
            return {'status':'no found'}, 404

    def put(self, tpl_key):
        """
        The update of template meta is disallowed to the key, only to the other properties.
        """
        args = parser.parse_args()
        document=json.loads(args['template_meta'])
        document['key']=tpl_key
        if self.templateService.updateTemplateMetaByKey(tpl_key, document)==1:
            return {'status':'ok'}, 200
        else:
            return {'status':'no found'}, 404


class TemplateSessionList(Resource):

    def __init__(self):
        self.templateService=TemplateService()

    def get(self):
        """
        Return all templates sessions of survey stored in the server
        """
        templates=self.templateService.getAllSessions()
        if templates==False:
            return {'status':'no found'}, 404
        else:
            return templates, 200

    def post(self):
        """
        Receive a survey template and store in the server
        """
        # check if the post request has the survey template document
        if 'template_session' not in request.form:
            # No template_session
            error_msg = 'Error in TemplateSessionList class when trying test the template_session from request. Return HTTP:500'
            logWriter(os.path.abspath(os.curdir) + LOG_PATH).write(error_msg)
            return {'status': 'parse error'}, 500
        template_session = request.form['template_session']
        if template_session == '':
            error_msg = 'Error in TemplateSessionList class when trying read the template_session. Return HTTP:500'
            logWriter(os.path.abspath(os.curdir) + LOG_PATH).write(error_msg)
            return {'status': 'missing document'}, 500
        if self.templateService.addSession(template_session):
            return {'status':'ok'}, 200
        else:
            return {'status': 'store error'}, 500

class TemplateSession(Resource):

    def __init__(self):
        self.templateService=TemplateService()
    
    def get(self, tpl_key):
        aTplSession=self.templateService.getTemplateSessionByKey(tpl_key)
        return aTplSession, 200

    def delete(self, tpl_key):
        """
        When remove one survey session the related survey templates will be remove too.
        It's allowed only if no forms uses the template.
        """
        if self.templateService.removeTemplateByKey(tpl_key)==1:
            return {'status':'ok'}, 200
        else:
            return {'status':'no found'}, 404

    def put(self, tpl_key):
        """
        The update of template session is disallowed to the key, only to the other properties.
        """
        args = parser.parse_args()
        document=json.loads(args['template_session'])
        document['key']=tpl_key
        if self.templateService.updateTemplateSessionByKey(tpl_key, document)==1:
            return {'status':'ok'}, 200
        else:
            return {'status':'no found'}, 404

# GET and POST Photos related with forms by survey_key
api.add_resource(Photo, '/photo/<survey_key>/<photo_id>')

# receive and delivery the JSON data as a survey metadata
api.add_resource(SurveyMetaList, '/meta')
api.add_resource(SurveyMeta, '/meta/<survey_key>')
# receive and delivery the JSON data as a survey form instance
api.add_resource(SurveyList, '/survey')
api.add_resource(Survey, '/survey/<survey_key>')
# delivery a list of surveys that match with the filters
api.add_resource(SurveySearch, '/survey/search/<start_date>/<end_date>/<status>/<type>/<custom>/<code>')

# delivery the list of Template types
api.add_resource(TemplateTypeList, '/template/type')
api.add_resource(TemplateType, '/template/type/<key>')
# delivery the list of  metadata to the Template
api.add_resource(TemplateMetaList, '/template/meta')
api.add_resource(TemplateMeta, '/template/meta/<key>')
# delivery the list of sessions and it's questions to the Template
api.add_resource(TemplateSessionList, '/template/session')
api.add_resource(TemplateSession, '/template/session/<key>')

if __name__ == '__main__':
     app.run(host=SERVER_IP, port=5000)