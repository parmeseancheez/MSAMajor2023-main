import flask
from flask import request, jsonify
import student_class_generator_v2

#Create an app
app = flask.Flask(__name__)

#Auto reload server when changes made
app.config["DEBUG"]

#load student dictionaries
student_dictionaries = student_class_generator_v2.get_student_dictionaries()

@app.route('/', methods=['GET'])
def index():
    return "<h1>My name is Sean Cajigal</h1>"

#Create route to return all student data
@app.route('/api/students/all', methods=['GET'])
def api_all():
    return jsonify(student_dictionaries)

app.run()