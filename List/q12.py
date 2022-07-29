#printing the last five and first five of the list with it's values squared
my_list =[23,2,4,33,4,23,23,223,55,53,343,6,34,2,64,5,45]
new_list = []
for list in my_list:
    new_list.append(list**2)
print(new_list[:5])
print(new_list[-5:])

