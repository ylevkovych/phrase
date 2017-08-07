
'''
Language route controller
'''

import app as app
from flask import render_template

@app.app.route("/language")
def languages():
    return render_template("language.html")
