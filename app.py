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

    #get student data
    student_data = get_student_data(url)

    return render_template('index.html', student_data = student_data)

@app.route('/majors', methods=['GET','POST'])
def majors():
    #make a request to the student api url
    url = 'http://127.0.0.1:5000/api/students/all'

    #get student data
    student_data = get_student_data(url)

    #student_data = [*range(0,10000000, 3)]
    
    #Write code that gets the unique majors from the student_data list
    major_list = []
    for student in student_data:
        if student['major'] not in major_list:
            major_list.append(student['major'])
    
    if request.method == 'POST':
        #get the form data
        major = request.form['major'].strip()

        result_list = []
        if not major:
            #flash("You must a select a major")
            pass
        else:
            #get student with selected major and palce in result list
            for student in student_data:
                if student['major'] == major:
                    result_list.append(student)
            return render_template('majors.html', major_list = major_list, result_list = result_list)

    return render_template('majors.html',major_list=major_list)

#Run the flask application
app.run(port=5007)