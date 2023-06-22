class Automobile():
    #1. Polymorphism
    #2. Inheritance
    #3. Encapsulation

    #Define a constructor
    #The constructor defines what happens when we create an automobile
    def __init__(self, make, model, vin, engine_size, owner, year):
        #assign parameter values
        self.__make = make
        self.__model = model
        self.__vin = vin
        self.__engine_size = engine_size
        self.__owner = owner
        self.__year = year
    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_vin(self):
        return self.__vin
    
    def get_engine_size(self):
        return self.__engine_size
    
    def set_engine_size(self, new_size):
        self.__engine_size = new_size
    
    def get_owner(self):
        return self.__owner

    def set_owner(self, new_owner):
        self.__owner = new_owner
    
    def get_year(self):
        return self.__year
    
    def get_age(self, current_year):
        return current_year - self.get_year()

    #Create a method to print Automobile data
    def printData(self):
        print(f"{self.year} {self.make} {self.model}")
        print(f"VIN: {self.vin}, Engine Size: {self.engine_size}")
        print(f"Owner: {self.owner}\n")