from flask import Flask, render_template, request, url_for, redirect, abort
import requests

#Make a Flask app
app = Flask(__name__)
app.config['DEBUG'] = True

#set secret key
app.config["SECRET_KEY"] = 'my secret key'

#Function to request student data form the api
#Input: url
#output: JSON
def get_student_data(url):
    #make a request
    response = requests.get(url)
    
    #convert format to json
    response_json = response.json()
    return response_json

#Create route for site index. Will display all student data
@app.route('/', methods=['GET'])
def index():
    #make a request to the student api url
    url = 'http://127.0.0.1:5000/api/students/all'

    student_data = get_student_data(url)
    return render_template('index.html', student_data = student_data)

app.run(port=5007)