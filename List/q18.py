# append a first list with the second list

first_list = [12,23,34,6,56,23,234,46,35,23,334,5,45]
second_list = [234,5,5,45,6,5,6,5,234,34,57,5,235,34,234]

for item in second_list:
    first_list.append(item)
print(first_list)