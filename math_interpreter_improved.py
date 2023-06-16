#Ask the user if they want to continue. If y, continue. If n, end.


def main():
    while True:
        # Prompt the user for the expression
        try:
            expression = input("Expression pls: ")

            # Use .split() to get the parts of the expression. Split at the space
            inputs = expression.split(" ")

            if len(inputs) != 3:
                print("ERROR: Enter expression in (x y z) format!\n")
                continue
            else:
                pass

            # Get values from list
            x = int(inputs[0])
            y = inputs[1]
            z = int(inputs[2])

            if y not in ["+","-","*","/"]:
                print("ERROR: Incorrect operator. Only (+,-,*,/) allowed\n")
                continue

        except ValueError:
            continue
        
        # Determine the type of operation to carry out. Using if/elif/else statement
        # Run the expression and print output formatted to one demical place 
        if y == "+":
            print(f"{x+z:.1f}")
        elif y == "-":
            print(f"{x-z:.1f}")
        elif y == "*":
            print(f"{x*z:.1f}")
        elif y == "/":
            print(f"{x/z:.1f}")
        
        another_calculation = input("Would you like to re-evaluate another expression? (y/n)")

        if another_calculation.lower() == "n":
            break
main()