my_list=[3,4235,23,234,3,3,4,34,52,35,2,5,300,2,235,235,35,6,235,5,34,4]

# largest = 0
# for item in my_list:
#     if item > largest:
#         largest = item
        

# print(largest)

list = sorted(my_list,reverse=True)
print('second largest element in this list is '+ str(list[1]))