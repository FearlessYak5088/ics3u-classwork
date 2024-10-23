# Write a program that creates a list of ten integers. It should put ten random numbers from 1 to 100 in the list. 
# It should copy all the elements of that list into another list of the same size. Then display the contents of both lists. 
# To get the output to look like mine, you’ll need a several for loops.

# Create a list of ten integers
# Fill the list with ten random numbers (1-100)
# Copy the list into another list of the same capacity
# Change the last value in the first list to a -7
# Display the contents of both lists

import random

# Make 2 empty lists
list1 = []
list2 = []

# Fill list1 with ten random numbers from 1-100
for i in range(10):
    list1.append(random.randint(1,100))

# Copy list1 into list2
for n in range(len(list1)):
    list2.append(list1[n])

# Change the last value of list1 to -7
list1[-1] = -7

# Print both lists
print(f"list 1: {list1}\nlist 2: {list2}")

# Find out and explain why you can’t copy a list by doing something like this:

# list1 = [5, 6, 7, 8]
# list2 = list1

# It doesnt work because list2 will always = list1, so when list1 changes, list2 also changes
