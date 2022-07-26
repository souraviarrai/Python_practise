# Write a Python program to multiply all the items in a list.


my_list = [34,55,37,3,456,6734,345]

def product_of_list(items):
    product = 1
    for item in items:
        product *= item
    return product

print(product_of_list(my_list))