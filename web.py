import flask
from flask import request, jsonify
import student_class_generator_v2

#Create an app
app = flask.Flask(__name__)

#Auto reload server when changes made
app.config["DEBUG"]


@app.route('/', methods=['GET'])
def index():
    return "<h1>My name is Sean Cajigal</h1>"

app.run()