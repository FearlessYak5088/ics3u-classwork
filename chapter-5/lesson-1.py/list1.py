# Create an empty list. You must use a loop to append the value -113 into the list ten times.
# Additionally, create a second loop below the first that will iterate through the list and print out each element. 
# Do not use a literal number in the range() function, you must use the len() function to inform the range function how many index numbers to generate.

# Create empty list
list = []

# Use list.append() to add values in the list
list.append(-113)
list.append(-113)
list.append(-113)
list.append(-113)
list.append(-113)
list.append(-113)
list.append(-113)
list.append(-113)
list.append(-113)
list.append(-113)

# Prints the slot number and value of the slot for each object in the list
for i in range(len(list)):
    print(f"Slot {i} contains a {list[i]}")
