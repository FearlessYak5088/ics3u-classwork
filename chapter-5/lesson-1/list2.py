# Create an empty List. Append ten random numbers from 1 to 100. Then display the contents of the list on the screen. You must use a loop.
# And, like last time, you must use the len() function and not a literal number (like 10) in loop range.

import random

# Create empty list
list = []

# Add 10 integers in the list (from 1 to 100)
list.append(random.randint(1,100))
list.append(random.randint(1,100))
list.append(random.randint(1,100))
list.append(random.randint(1,100))
list.append(random.randint(1,100))
list.append(random.randint(1,100))
list.append(random.randint(1,100))
list.append(random.randint(1,100))
list.append(random.randint(1,100))
list.append(random.randint(1,100))

# Print each slot number in the list in order and their value
for i in range(len(list)):
    print(f"slot {i} contains a {list[i]}")
