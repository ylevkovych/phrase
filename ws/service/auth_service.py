
import json
import dao.user_dao as user_dao
import dao.user_settings_dao as user_settings_dao
import app as app
from flask import session

USERNAME_FIELD_NAME = 'username'
PASSWORD_FIELD_NAME = 'password'

USER_SETTINGS_SESSION_NAME = 'user_settings'


def login(request):
    
    creds = _get_creds(request)
    
    if (not _validate_creds(creds)):
        return None

    user = user_dao.fetchone_by_username(creds[USERNAME_FIELD_NAME])
    
    if (user is None):
        return None

    user_settings = user_settings_dao.fetch_one_by_user_id(user._id)
    
    if (user_settings is None):
        return None
    
    _set_session(user_settings)

    return user_settings

def logout():
    if app.session and USER_SETTINGS_SESSION_NAME in app.session:
        app.session[USER_SETTINGS_SESSION_NAME] = None

    return True
    
def _set_session(user_settings):
    app.session[USER_SETTINGS_SESSION_NAME] = json.dumps(user_settings, default = lambda o: o.__dict__)
    

def _validate_creds(creds):
    
    if creds[USERNAME_FIELD_NAME] == None or creds[PASSWORD_FIELD_NAME] == None:
        return False

    user = user_dao.fetchone_by_username_and_password(
        creds[USERNAME_FIELD_NAME], creds[PASSWORD_FIELD_NAME])

    if not user:
        return False

    return True


def _get_creds(request):
    
    creds = {
        USERNAME_FIELD_NAME: None,
        PASSWORD_FIELD_NAME: None
    }
    
    args = request.args
    data = request.data
    form_data = request.form

    found_data = False

    if (not found_data and args):
        creds[USERNAME_FIELD_NAME] = args[USERNAME_FIELD_NAME]
        creds[PASSWORD_FIELD_NAME] = args[PASSWORD_FIELD_NAME]
        
        found_data = True

    if (not found_data and data):
        json_data = json.loads(data)
        if (json_data):        
            creds[USERNAME_FIELD_NAME] = json_data[USERNAME_FIELD_NAME]
            creds[PASSWORD_FIELD_NAME] = json_data[PASSWORD_FIELD_NAME]

            found_data = True

    if (not found_data and form_data):
        creds[USERNAME_FIELD_NAME] = form_data[USERNAME_FIELD_NAME]
        creds[PASSWORD_FIELD_NAME] = form_data[PASSWORD_FIELD_NAME]

        found_data = True

    return creds
