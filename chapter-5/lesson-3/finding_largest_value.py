# Write a program that creates a list to hold random numbers from 1 to 100. Display the values in the list on the screen. 
# Then use a linear search to find the largest value in the list, and display that value.

import random

nums = []

for i in range(10):
    nums.append(random.randint(1,100))

max_value = 0

for n in nums:
    if n > max_value:
        max_value = n

print(f"List: {nums}\nThe largest value is {max_value}")
