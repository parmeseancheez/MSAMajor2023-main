class Student():
    def __init__(self, first_name, last_name, major, credit_hours, gpa, id_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__id_number = id_number

    def get_class_level(self):
        if self.__credit_hours > 90:
            return "Freshman"
        elif self.__credit_hours >= 61:
            return "Sophomore"
        elif self.__credit_hours <= 31:
            return "Junior"
        else:
            return "Senior"
    
    def update_credit_hours(self, hours):
        self.__credit_hours += hours

    def print_student_data(self):
        print(self.__first_name, self.__last_name, self.__major, self.__credit_hours, self.__gpa, self.__id_number)