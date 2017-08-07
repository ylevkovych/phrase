import app as app

@app.app.route("/")
def index():
    return "Hello World"


