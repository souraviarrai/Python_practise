# check if the list is cicularly identical or not


list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

def checker_circular(lis1,lis2):
    answer = ' '.join(map(str,lis1)) in ' '.join(map(str,lis2 * 2))
    return answer

if checker_circular(list1,list3):
    print('They are circular')
else:
    print('They are not circular')
