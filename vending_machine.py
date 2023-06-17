def awaitCoin():
    while True:
        userInput = int(input("Please insert coins:\n"))
        if userInput not in [1,5,10,25]:
            print("Must input 1, 5, 10, or 25")
        else:
            return userInput

def awaitCost(cost):
    print(f"um gimme {cost} (in cents)")
    amountInserted = 0
    while amountInserted < cost:
        amountInserted+=awaitCoin()
        if amountInserted > cost:
            break
        print(f"Amount STILL due: {cost-amountInserted}")
    print("Thanks! Enjoy your MTN DEW KICKSTART® BLACK CHERRY")

awaitCost(50)