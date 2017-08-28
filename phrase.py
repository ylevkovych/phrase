

from flask import Flask, session
import app as app
import hashlib

app.app = Flask(__name__,template_folder="ui")
app.session = session

from ws.controller import index
from ws.controller import user
from ws.controller import user_api
from ws.controller import language
from ws.controller import language_api
from ws.controller import folder
from ws.controller import folder_api
from ws.controller import login_api

app.app.secret_key = hashlib.sha256(b'ferofj2387Xxjo23ij23').hexdigest()

if (__name__ == '__main__'):
    app.app.run(debug=True)
