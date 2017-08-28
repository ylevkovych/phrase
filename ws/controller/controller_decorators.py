import app as app
import ws.controller.api_helper as api_helper
from functools import wraps

def check_auth_api(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if _authenticated():
            return fn(*args, **kwargs)
        return api_helper.get_401_resp()
            
    return wrapper
        

def check_auth(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if _authenticated():
            return fn(*args, **kwargs)
        return api_helper.get_401_resp()
            
    return wrapper


def _authenticated():
    return True if app.session and app.session['user_settings'] else False
            