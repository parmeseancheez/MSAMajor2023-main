import automobile

#Create an automobile
auto1 = automobile.Automobile("Mercury")
auto2 = automobile.Automobile("Honda")

auto_list = []
auto_list.append(auto1)
auto_list.append(auto2)

for auto in auto_list:
    print(auto.make)
    print(auto.model)
    print()