#Write a Python program to get the difference between the two lists.
list_1 = [234,25,345,343,6,2346,34636,3623,233,235,6]
list_2 = [553,45,563,573,346,363,3463,346,435,75,346]


diff_list1_list2 = list(set(list_1) - set(list_2))
diff_list2_list1 = list(set(list_2) - set(list_1))
total = diff_list1_list2 + diff_list2_list1
print(total)



    
