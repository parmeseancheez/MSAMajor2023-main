#Reading files in python
#Open the file
data_file = open("file.txt", "r")

#Create an empty dictionary
menu_items = {}

for line_of_data in data_file:
    print(line_of_data)
    #what do we need to do to each line of data?
    #split line of data at the ", "
    key_values = line_of_data.split(", ")

    #create an entry to the dictionary. Remeber to convert price to float.
    menu_items[key_values[0]] = float(key_values[1])
print(menu_items)
data_file.close()

for item, price in menu_items.items():
    print(f"{item}: ${price:.2f}")
    #not done