# sample_list = [6,4,3,7,1,9,8,12]


# def bubble_sort(liss):
#     for i in range(0,len(liss)):
#         for j in range(0,len(liss)-i-1):
#             if liss[j] > liss[j+1]:
#                 temp = liss[j+1]
#                 liss[j+1] = liss[j]
#                 liss[j] = temp
#     return liss

# print(bubble_sort(sample_list))


from q6 import bubble_sort


arr = [64, 34, 25, 12, 22, 11, 90]


def bubble(list_items):
    for i in range(0,len(list_items)):
        for j in range(0,len(list_items)-i-1):
            if(list_items[j]>list_items[j+1]):
                temp = list_items[j+1]
                list_items[j+1] = list_items[j]
                list_items[j] = temp
    return list_items

print(bubble_sort(arr))
