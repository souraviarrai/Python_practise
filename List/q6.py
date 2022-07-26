#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples


# from numpy import sort




# def order_by_second_element(items):
#     new_list = []
#     for item in items:
#         for i in item:
#             if(item[i][1]>item[i+1][1]):
#                 my_list =  
#     return new_list
# print(order_by_second_element(my_list))

# Method One - by using sorted

# def last(n):
#     return n[-1]

# def sort(lis):
#     return sorted(lis,key=last)

# print('sorted')
# print(sort(my_list))


# Method Two - bubble sort


my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def bubble_sort(list_items):
    for i in range(0,len(list_items)): 
        for j in range(0,len(list_items)-i-1):
            if(list_items[j][1]>list_items[j+1][1]):
                temp = list_items[j+1]
                list_items[j+1] = list_items[j]
                list_items[j] = temp
    return list_items

print('The new sorted list tuple are : '+ str(bubble_sort(my_list)))