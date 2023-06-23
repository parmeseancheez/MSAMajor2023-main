import flask

app = flask.Flask(__name__)
app.config["DEBUG"]

@app.route('/', methods=['GET'])
def index():
    return "<h1>My name is Sean Cajigal</h1>"

app.run()