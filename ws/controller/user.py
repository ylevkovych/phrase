
'''
User route controller
'''

import app as app
from flask import render_template

@app.app.route("/user")
def users():
    return render_template("user.html")
