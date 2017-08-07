

from flask import Flask
import app as app

app.app = Flask(__name__,template_folder="ui")

from ws.controller import index
from ws.controller import user
from ws.controller import user_api
from ws.controller import language
from ws.controller import language_api
from ws.controller import folder
from ws.controller import folder_api

if (__name__ == '__main__'):
    app.app.run(debug=True)
