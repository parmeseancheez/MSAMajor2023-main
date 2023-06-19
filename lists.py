#List demo
demo_list = [10, 16, 24, 77, 2, 14, 9]

#Add values to the list
demo_list.append(5)
demo_list.append(63)
print(demo_list)

#Get number of items in list
print(len(demo_list))

#Get values from the list
#Get first value from the list
print(demo_list[0])

for item in demo_list:
    print(item)

#Declare a car dictionary
car = {"make": "Mercury", "model": "Sable", "year": 1998, "value": "10000", "engine": 3.0}

#Get all the keys, values from the student score dictionary
for student in student_scores:
    print(f"{student}: {student_scores[student]}")
