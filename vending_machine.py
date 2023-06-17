def awaitCost(cost):
    print(f"um gimme {cost} (in cents)")
    amountInserted = 0
    while amountInserted < cost:
        userInput = input(f"Amount due: {cost-amountInserted}\nPlease insert coins:\n")
        amountInserted+=userInput
awaitCost(50)