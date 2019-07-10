from survey_service import SurveyService

surveyService=SurveyService()

survey_meta="""{"icon":"","key":"22062019192950","surveyType":"landslide","status":"Pré-cadastrada","selected":false,"origin":"app","date":"2019-06-22T22:30:01.588Z"}"""
survey_document="""{"key":"22062019192950","formData":{"type":"landslide","location":{"coords":{"lat":-23.179264,"lng":-45.8752}},"sessionsCompleted":["s7","s8","s9"],"status":false,"grau_risco":"option-3","moradias_risco":null,"pessoas_remocao":null,"outras_informacoes":"ssasasas","equipe":"juritis","numero_ocorrencia":"22062019192950"}}"""

surveyService.addSurveyAndMeta(survey_document, survey_meta)