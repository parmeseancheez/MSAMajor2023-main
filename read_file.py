#Reading files in python
#Open the file
data_file = open("file.txt", "r")

#Create an empty dictionary
menu_item = {}

for line_of_data in data_file:
    #what do we need to do to each line of data?
    #split line of data at the ", "
    key_values = line_of_data.split(", ")

    #create an entry to the dictionary. Remeber to convert price to float.
    menu_item[key_values[0]] = float(key_values[1])

#close file
data_file.close()

for item, price in menu_item.items():
    print(f"{item}: ${total:.2f}")
    #not done