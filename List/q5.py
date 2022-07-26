#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

sample_list = ['abc', 'xyz', 'aba', '1221','45674','wertyw']

def string_counter(items):
    counter = 0
    for item in items:
        if len(item)>2 and item[0] == item[-1]:
            counter += 1
    return counter
print(string_counter(sample_list))