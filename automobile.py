class Automobile():
    #Define a constructor
    #The constructor defines what happens when we create an automobile
    def __init__(self, make, model, vin, engine_size, owner, year):
        #assign parameter values
        self.make = make
        self.model = model
        self.vin = vin
        self.engine_size = engine_size
        self.owner = owner
        self.year = year

    #Create a method to print Automobile data
    def printData(self):
        print(f"{self.year} {self.make} {self.model}")
        print(f"VIN: {self.vin}, Engine Size: {self.engine_size}")
        print(f"Owner: {self.owner}\n")