def get_dictionary():
    data_file = open("file.txt", "r")

    menu_items = {}

    for line_of_data in data_file:
        print(line_of_data)
        #what do we need to do to each line of data?
        #split line of data at the ", "
        key_values = line_of_data.split(", ")

        #create an entry to the dictionary. Remeber to convert price to float.
        menu_items[key_values[0]] = float(key_values[1])
    
    data_file.close()
    return menu_items

def orderFood():
    menu = get_dictionary() 
    total = 0
    while True:
        prompt = input(f"Total: ${total:.2f} | Item: ").title()
        if prompt in menu.keys():
            total += menu[prompt]
        elif prompt == "End":
            print("\nEnjoy your meal!")
            break
        else:
            print("Sorry we dont have that... It's probably at McDonald's")

def main():
    orderFood()

main()