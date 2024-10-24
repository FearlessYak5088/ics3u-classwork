# Create a list and place in it ten random values from 1-50. 
# Display those values on the screen, and then prompt the user for an integer. 
# Search through the list, and if the item is present, say so. 
# If the value is not in the list, display a single message saying so. 
# Just like the previous assignment, if the value is present more than once, you may display the message as many times as necessary.

import random

list = []

for i in range(10):
    list.append(random.randint(1,50))

print(f"List: {list}")
usernum = int(input("Value to find: "))

for j in range(len(list)):
    if usernum == list[j]:
        print(f"{usernum} is in the list.")
    elif usernum not in list:
        print(f"{usernum} is not in the list.")
        break
