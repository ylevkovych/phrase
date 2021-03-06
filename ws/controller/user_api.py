
'''
User REST API
'''

import ws.controller.api_helper as api_helper
import ws.controller.controller_decorators as controller_decorators
import app as app
import dao.user_dao as user_dao
import dao.user_settings_dao as user_settings_dao
import entity.user as user_entity
import entity.user_settings as user_settings_entity
import ws.service.user as user_service
from flask import request

@app.app.route("/rest/api/v1.0/user", methods=["GET"])
@controller_decorators.check_auth_api
def get_users():
    page = request.args.get("page")
    items = request.args.get("items")
    
    users = user_dao.fetchall(page=page, items=items)

    return api_helper.get_json_resp(users)


@app.app.route("/rest/api/v1.0/user/<userId>", methods=["GET"])
def get_user(userId):
    user = user_dao.fetchone(userId)

    if (user is None):
        return api_helper.get_404_resp("User not found")

    return api_helper.get_json_resp(user)


@app.app.route("/rest/api/v1.0/user/name/<name>", methods=["GET"])
@controller_decorators.check_auth_api
def get_user_by_name(name):
    user = user_dao.fetchone_by_username(name)

    if (user is None):
        return api_helper.get_404_resp("User not found")

    return api_helper.get_json_resp(user)


@app.app.route("/rest/api/v1.0/user", methods=["POST"])
@controller_decorators.check_auth_api
def add_user():
    user = user_service.get_user_from_data(request.data)

    if (user == None):
        return api_helper.get_412_resp()

    user_dao.create(user)

    if (user._id):
        user_settings = user_settings_entity.UserSettings()
        user_settings.userId = user._id
        user_settings.roleId = 2
        user_settings.language1Id = 10
        user_settings.language1Id = 11

        user_settings_dao.create(user_settings)

    return api_helper.get_json_resp(user)

@app.app.route("/rest/api/v1.0/user/<userId>", methods=["PUT"])
@controller_decorators.check_auth_api
def update_user(userId):
    user = user_service.get_user_from_data(request.data)

    if (user == None):
        return api_helper.get_412_resp()

    if (user_dao.fetchone(userId) is None):
        return api_helper.get_404_resp("User not found")

    user._id = userId

    user_dao.update(user)

    return api_helper.get_json_resp(user)


@app.app.route("/rest/api/v1.0/user/<userId>", methods=["DELETE"])
@controller_decorators.check_auth_api
def delete_user(userId):
    
    if (user_dao.fetchone(userId) is None):
       return api_helper.get_404_resp("User not found")

    user_dao.delete(userId)

    if (user_dao.fetchone(userId) is not None):
           return api_helper.get_412_resp("User has not been removed")

    return api_helper.get_json_resp(True)
