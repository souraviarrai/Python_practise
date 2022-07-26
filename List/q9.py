# write a function that checks if the items in the two given list have same members

lis1= [1,34,34,243,534,23]
lis2= [2,32,343,55,353,32]
def checker(first_list,second_list):
    counter = False
    for item in first_list:
        for ktem in second_list:
            if item == ktem:
                counter = True
    return counter

def cross_checker():
    if checker(lis1,lis2) == True:
        print('There are duplicates')
    else:
        print('no duplicates')

cross_checker()



                 