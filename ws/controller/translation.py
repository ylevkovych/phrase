
'''
Translation route controller
'''

import app as app
from flask import render_template

@app.app.route("/tranlation")
def translations():
    return render_template("translation.html")
