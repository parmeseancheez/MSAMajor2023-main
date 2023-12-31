import student_class
from datetime import datetime

try:
    data_file = open("students.csv", "r")
except Exception:
    print("Error opening file.")

def write_to_error_log(message):
    try:
        #open log file
        log_file = open("error_log.txt", "a")
        log_file.write(f"{str(datetime.now())}: {message}\n")
        log_file.close()
    except Exception as err:
        print(err)
        return
    return
"""
Function to return list of student objects
Input: none
Output: list of student objects
"""


def load_students():
    students = []
    for line_of_data in data_file:
        try:
            print(line_of_data)
            key_values = line_of_data.split(",")
            if len(key_values) == 6:
                students.append(student_class.Student(key_values[0], key_values[1], key_values[2], int(key_values[3]), float(key_values[4]), int(key_values[5])))
        except Exception as error:
            write_to_error_log(error)
    
    return students

    data_file.close()

    for student in students:
        print(student.print_student_data())
"""
Function to convert student object to student dictionaries
Input: List of Student objects
Output: List of student dictionaries
"""
def student_to_dictionary(students):
    #create a list to store the dictionaries
    student_dictionary_list = []

    #loop through student list and write each student's data to a dictionary
    for student in students:
        student_dictionary = {}
        #Set keys and values for first name, last name, name, ID, major, gpa, class level
        student_dictionary['id'] = student.get_ID()
        student_dictionary['first_name'] = student.get_first_name()
        student_dictionary['last_name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_gpa()
        student_dictionary['class_level'] = student.get_class_level()

        student_dictionary_list.append(student_dictionary)

    return student_dictionary_list

def get_student_dictionaries():
    #get a list of students
    student_list = load_students()

    #get list of student dictiontaries
    student_dictionaries = student_to_dictionary(student_list)

    return student_dictionaries

        


    
