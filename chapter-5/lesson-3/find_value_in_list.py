# Create a list with ten random values from 1-50. Display those values on the screen, and then prompt the user for an integer. 
# Search through the list, and if the item is present, say so. It is not necessary to display anything if the value was not found. 
# If the item is in the list multiple times, it’s okay if the program prints the message more than once.

import random

list = []

for i in range(10):
    list.append(random.randint(1,50))

print(f"List: {list}")
usernum = int(input("Value to find: "))

for j in range(len(list)):
    if usernum == list[j]:
        print(f"{usernum} is in the list.")
