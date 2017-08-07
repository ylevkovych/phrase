
'''
Folder route controller
'''

import app as app
from flask import render_template

@app.app.route("/folder")
def folders():
    return render_template("folder.html")
