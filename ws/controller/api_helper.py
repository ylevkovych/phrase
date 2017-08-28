
'''
API Helper
'''

from flask import Response, json, jsonify


def get_json_resp(data):
    resp = Response(json.dumps(data, default=lambda o: o.__dict__))
    resp.headers["Content-Type"] = "application/json"
    
    return resp

def get_401_resp():
    return _get_resp("Not authorized", 401)

def get_404_resp(msg="Resource not found"):
    return _get_resp(msg, 404)
    
def get_412_resp(msg="Wrong data in request payload"):
    return _get_resp(msg, 412)

def _get_resp(msg, status_code=200):
    resp = jsonify({"message": msg})
    resp.status_code = status_code
    return resp
