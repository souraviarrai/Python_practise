# flatten a list
import itertools
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]

# new_list = list(itertools.chain(*original_list))
# print(new_list)

list_new = []
for item in original_list:
    for i in item:
        list_new.append(i)
print(list_new)