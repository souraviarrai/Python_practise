#Write a Python program to print the numbers of a specified list after removing even numbers from it.

lis1= [1,34,34,243,534,23]

new_list = []
for item in lis1:
    if item % 2 == 0:
        lis1.remove(item)
    else:
        new_list.append(item)
print(new_list)
            