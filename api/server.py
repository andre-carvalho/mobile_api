import os
import json
from flask import Flask, request, send_from_directory
from flask_restful import abort, Api, Resource
from werkzeug.utils import secure_filename
from flask_cors import CORS
#from storage_module.midias_dao import MidiasDao
from logs_module.log_writer import logWriter

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
    def get(self):
        """
        Return all survey meta stored in the server
        """

    def post(self):
        """
        Receive a survey meta and store in the server
        """

class SurveyMeta(Resource):
    def get(self, survey_key):
        aSurveyMeta=getSurveyMetaByKey(survey_key)
        return aSurveyMeta

    def delete(self, survey_key):
        removeSurveyMetaByKey(survey_key)
        return '', 204

    def put(self, survey_key):
        args = parser.parse_args()
        aSurveyMeta=updateSurveyMetaByKey(survey_key, args['meta'])
        return aSurveyMeta, 201

class SurveyList(Resource):

class Survey(Resource):

class SurveySearch(Resource):

# Template classes
class TemplateTypeList(Resource):

class TemplateType(Resource):

class TemplateMetaList(Resource):

class TemplateMeta(Resource):

class TemplateSessionList(Resource):

class TemplateSession(Resource):


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