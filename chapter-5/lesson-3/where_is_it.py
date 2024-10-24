# Create a list to hold ten random values from 1-50. Display those values on the screen, and then prompt the user for an integer. 
# Search through the list, and if the item is present, give the index position of where it is located. 
# If the value is not in the list, display a single message saying so. 
# If the value is present more than once, you may either display the message as many times as necessary, 
# or display a single message giving the last index position in which it appeared.

# Display the message as many times
import random

list = []

for i in range(10):
    list.append(random.randint(1,50))

print(f"List: {list}")
usernum = int(input("Value to find: "))

for j in range(len(list)):
    if usernum == list[j]:
        print(f"{usernum} is in the list at index {j}.")
    elif usernum not in list:
        print(f"{usernum} is not in the list.")
        break

# Single message giving last index position
import random

list = []

for i in range(10):
    list.append(random.randint(1,50))

print(f"List: {list}")
usernum = int(input("Value to find: "))

for j in range(len(list)):
    if usernum == list[j]:
        last_index = j
    elif usernum not in list:
        print(f"{usernum} is not in the list.")
        break
print(f"{usernum}'s last index is at {last_index}.")
