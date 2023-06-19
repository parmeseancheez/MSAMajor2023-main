def orderFood():
    menu = {"Baja Taco": 4.00, "Burrito": 7.50, "Bowl": 8.50, "Nachos": 11.00, "Quesadilla": 8.50, "Super Burrito": 8.50, "Super Quesadilla": 9.50, "Taco": 3.00, "Tortilla Salad": 8.00}
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