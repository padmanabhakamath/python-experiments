import sys
## List of python katas to familiarize with from time to time
## Delete all code (except comments) to start afresh

# Create a list, a set, a tuple and a dictionary
# Explain the difference
fruits = ['apple', 'oranges', 'bananas'] # list
fruits.append('kurch')
print(fruits)

set = {'fruits', 'oranges', 'bananas','oranges'} #set

set.add('blanco')
print(set) # unordered. 


tuple = ('eagle', 'pigeon', 'fruitfly')
tuple2 = ('tret',)
tuple += tuple2
print(tuple)


# Create two lists and zip them up
list1 = ['tera', 'treay', 'creay']
list2 = ['mera', 'breay', 'freay']
list_final = zip(list1, list2)
print('Final list: ', list(list_final))
print('Final list: ', list(list_final))


# function definition 
# Define a function that takes two string params and prints thos two params 
def printParams(first: str, second: str):
    print(first + second)

# print from 1 to 9 in a for loop using range function


# loop through a list of strings


# loop through a range of integers and sum each one with the rest before it
print('Adding up a million numbers .... ')

# Do list comprehension 
cubeList = [value**3 for value in range(1,11)]
print(cubeList)

print(sys.prefix)
