import sys
## List of python katas to familiarize with from time to time
## Delete all code (except comments) to start afresh

# Create a list, a tuple and a dictionary
# Explain the difference
justAList = ['t1', 't2', 't3', 6] # NOT immutable eg. justAList[1] = 'x' is ok
justAList[2] = 'x'
print(justAList)
tuple = (30, 60, 90, 'Treat') # Immutable. tuple[1] = 60 will throw an error 


# Create two lists and zip them up
fruits = ['apple', 'banana','grapes']
prices = [3, 4, 6]
combined = zip(fruits, prices)

print(list(combined))

# function definition 
# Define a function that takes two string params and prints thos two params 
def printd(animal: str, name: str):
    print(f'This is {animal}, my name is {name}')

printd('korma', 'chicken')

# print from 1 to 9 in a for loop using range function
for i in range(1, 10, ):
    print(i)

# loop through a list of strings
magicians = ['tert', 'bert', 'kurt']
for magician in magicians:
    print(magician)

print('Adding up a million numbers .... ')
i = 0
for j in range(1, 1000000):
    i = i+j

print('Adding up all million numbers .... ', i)

cubeList = [value**3 for value in range(1,11)]
print(cubeList)

print(sys.prefix)
