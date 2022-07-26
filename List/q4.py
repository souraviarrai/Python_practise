#Write a Python program to get the smallest number from a list





my_list = [34,55,37,3,456,6734,345]
def smallest_of_all(items):
    smallest = items[0]
    for item in items:
        if(item < smallest):
            smallest = item
    return smallest

print(smallest_of_all(my_list))