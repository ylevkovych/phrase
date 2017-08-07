
'''
Language REST API
'''

import ws.controller.api_helper as api_helper
import app as app
import dao.language_dao as language_dao
import entity.language as language_entity
import ws.service.language as language_service
from flask import request

@app.app.route("/rest/api/v1.0/language", methods=["GET"])
def get_languages():
    page = request.args.get("page")
    items = request.args.get("items")
    
    print ("page: "+str(page))
    print ("items: "+str(items))

    languages = language_dao.fetchall(page=page, items=items)

    return api_helper.get_json_resp(languages)


@app.app.route("/rest/api/v1.0/language/<languageId>", methods=["GET"])
def get_language(languageId):
    language = language_dao.fetchone(languageId)

    if (language is None):
        return api_helper.get_404_resp("language not found")

    return api_helper.get_json_resp(language)


@app.app.route("/rest/api/v1.0/language/name/<name>", methods=["GET"])
def get_language_by_name(name):
    language = language_dao.fetchone_by_languagename(name)

    if (language is None):
        return api_helper.get_404_resp("language not found")

    return api_helper.get_json_resp(language)


@app.app.route("/rest/api/v1.0/language", methods=["POST"])
def add_language():
    language = language_service.get_language_from_data(request.data)

    if (language == None):
        return api_helper.get_412_resp()

    if (language_dao.fetchone_by_name(language.name) is not None):
        return api_helper.get_412_resp("Item already exist")

    language_dao.create(language)

    return api_helper.get_json_resp(language)

@app.app.route("/rest/api/v1.0/language/<languageId>", methods=["PUT"])
def update_language(languageId):
    language = language_service.get_language_from_data(request.data)

    if (language == None):
        return api_helper.get_412_resp()

    if (language_dao.fetchone(languageId) is None):
        return api_helper.get_404_resp("language not found")

    language._id = languageId

    language_dao.update(language)

    return api_helper.get_json_resp(language)


@app.app.route("/rest/api/v1.0/language/<languageId>", methods=["DELETE"])
def delete_language(languageId):
    
    if (language_dao.fetchone(languageId) is None):
       return api_helper.get_404_resp("language not found")

    language_dao.delete(languageId)

    if (language_dao.fetchone(languageId) is not None):
           return api_helper.get_412_resp("language has not been removed")

    return api_helper.get_json_resp(True)
