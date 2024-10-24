# Create a list and store 10 random numbers from 1-50. 
# Display those values on the screen, and then prompt the user for an integer. 
# Search through the list, and count the number of times the item is found.

import random

list = []

for i in range(10):
    list.append(random.randint(1,50))

print(f"List: {list}")
usernum = int(input("Value to find: "))

count = 0
for j in range(len(list)):
    if usernum == list[j]:
        count += 1
if count >= 2 or count == 0:
    print(f"{usernum} was found {count} times.")
else:
    print(f"{usernum} was found {count} time.")
