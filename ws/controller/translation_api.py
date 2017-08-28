
'''
Translation REST API
'''

import ws.controller.api_helper as api_helper
import ws.controller.controller_decorators as controller_decorators
import app as app
import dao.translation_dao as translation_dao
import entity.translation as translation_entity
import ws.service.translation as translation_service
from flask import request

@app.app.route("/rest/api/v1.0/translation/user/<userId>/language1/<lnguage1Id>/language2/<language2Id>", methods=["GET"])
@controller_decorators.check_auth_api
def get_translations():
    page = request.args.get("page")
    items = request.args.get("items")
    
    print ("page: "+str(page))
    print ("items: "+str(items))

    translations = translation_dao.fetchall(page=page, items=items)

    return api_helper.get_json_resp(translations)


@app.app.route("/rest/api/v1.0/translation/<translationId>", methods=["GET"])
@controller_decorators.check_auth_api
def get_translation(translationId):
    translation = translation_dao.fetchone(translationId)

    if (translation is None):
        return api_helper.get_404_resp("Translation not found")

    return api_helper.get_json_resp(translation)


@app.app.route("/rest/api/v1.0/translation", methods=["POST"])
@controller_decorators.check_auth_api
def add_translation():
    translation = translation_service.get_translation_from_data(request.data)

    if (translation == None):
        return api_helper.get_412_resp()

    translation_dao.create(translation)

    return api_helper.get_json_resp(translation)

@app.app.route("/rest/api/v1.0/translation/<translationId>", methods=["PUT"])
@controller_decorators.check_auth_api
def update_translation(translationId):
    translation = translation_service.get_translation_from_data(request.data)

    if (translation == None):
        return api_helper.get_412_resp()

    if (translation_dao.fetchone(translationId) is None):
        return api_helper.get_404_resp("Translation not found")

    translation._id = translationId

    translation_dao.update(translation)

    return api_helper.get_json_resp(translation)


@app.app.route("/rest/api/v1.0/translation/<translationId>", methods=["DELETE"])
@controller_decorators.check_auth_api
def delete_translation(translationId):
    
    if (translation_dao.fetchone(translationId) is None):
       return api_helper.get_404_resp("Translation not found")

    translation_dao.delete(translationId)

    if (translation_dao.fetchone(translationId) is not None):
           return api_helper.get_412_resp("Translation has not been removed")

    return api_helper.get_json_resp(True)
