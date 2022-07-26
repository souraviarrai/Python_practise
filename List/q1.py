# Write a Python program to sum all the items in a list.




my_list = [34,55,37,3,456,6734,345]
# sum = 0
# for lis in my_list:
#     sum += lis
# print(sum)

def sum_of_list(my_list):
    sum = 0
    for item in my_list:
        sum += item
    return sum

print(sum_of_list(my_list))