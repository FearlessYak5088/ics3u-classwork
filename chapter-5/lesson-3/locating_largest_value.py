# Write a program that creates a list to hold random numbers from 1 to 100. Display the values in the array on the screen. 
# Then use a linear search to find the largest value in the array, and display that value and its index location.

import random

nums = []

for i in range(10):
    nums.append(random.randint(1,100))

max_value = 0

for n in range(len(nums)):
    if nums[n] > max_value:
        max_value = nums[n]
        index = n

print(f"List: {nums}\nThe largest value is {max_value}\nThe index is at {index}")
