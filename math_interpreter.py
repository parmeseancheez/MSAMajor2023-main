# Prompt the user for the expression
expression = input("Expression pls: ")

# Use .split() to get the parts of the expression. Split at the space
inputs = expression.split(" ")

# Get values from list
x = int(inputs[0])
y = inputs[1]
z = int(inputs[2])

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



