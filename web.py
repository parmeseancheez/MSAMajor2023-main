import flask

#Create an app
app = flask.Flask(__name__)

#Auto reload server when changes made
app.config["DEBUG"]


@app.route('/', methods=['GET'])
def index():
    return "<h1>My name is Sean Cajigal</h1>"

app.run()