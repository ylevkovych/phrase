import ws.controller.api_helper as api_helper
import ws.service.auth_service as auth_service
import app as app
from flask import request

@app.app.route("/rest/api/v1.0/login", methods = ["POST"])
def login():
    
    user_settings = auth_service.login(request)
    
    if not user_settings:
        return api_helper.get_401_resp()

    return api_helper.get_json_resp(user_settings)


@app.app.route("/rest/api/v1.0/logout", methods = ["POST"])
def logout():
    
    result = True if auth_service.logout() else False

    return api_helper.get_json_resp({"msg": result})
