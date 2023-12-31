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


students = []
for line_of_data in data_file:
    try:
        print(line_of_data)
        key_values = line_of_data.split(",")
        if len(key_values) == 6:
            students.append(student_class.Student(key_values[0], key_values[1], key_values[2], int(key_values[3]), float(key_values[4]), int(key_values[5])))
    except Exception as error:
        write_to_error_log(error)
    
data_file.close()

for student in students:
    print(student.print_student_data())
