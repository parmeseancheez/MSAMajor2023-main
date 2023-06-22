import automobile

#Create an automobile
auto1 = automobile.Automobile("Mercury", "Sable", "1234", 3.0, "Bob", 2000)
auto2 = automobile.Automobile("Honda", "Accord", "23456", 1234, "Alice", 2003)

#Change auto2 year
auto2.year = 2020

auto_list = []
auto_list.append(auto1)
auto_list.append(auto2)

#Print each automobile's info
for auto in auto_list:
    auto.print_data()

print(f"Auto1 is {auto1.get_age()} years old")