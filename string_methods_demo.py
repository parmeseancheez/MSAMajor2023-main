my_name = "sean"
print(my_name.capitalize())

print(my_name.upper())

print(my_name.startswith("se"))

print(my_name.endswith("ean"))

sentence = "I do not have a dog. My dog would be cute though. Do you want a dog?"

#for letter in sentence:
#    print(letter)

length = len(my_name)

###
term = "dog"
found_index = 0
term_count = 0
more_terms = True
while more_terms:
    found_index = sentence.find("term", found_index)
    if found_index != -1:
        term_count += 1
        found_index += 1
    else:
        more_terms = False

print(f"Number of terms: {term_count}")