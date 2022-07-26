#Write a Python program to get the largest number from a list.





my_list = [34,55,37,3,456,6734,345]

def largest_of_all(items):
    largest = 0 
    for item in items:
        if(item > largest):
            largest = item
    return largest

print(largest_of_all(my_list))