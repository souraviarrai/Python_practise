# Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included). 


list_no = []
for i in range(1,31):
    list_no.append(i**2)
print(list_no[5:])