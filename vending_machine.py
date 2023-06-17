cost = 50
print(f"um gimme {cost} (in cents)")

def awaitCost():
    amountInserted = 0
    while amountInserted < cost:
        userInput = input(f"Amount due: {cost-amountInserted}\nPlease insert coins:\n")
        amountInserted+=userInput