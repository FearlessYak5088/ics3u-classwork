# # Create an empty list. Fill the array with 1000 random numbers in the range 10-99. 
# Then display the contents of the list on the screen. You must use a loop (otherwise, good luck).
# If you’re careful to only pick random numbers from 10 to 99 and you put two spaces after each number when you print them, then your output will line up like mine.

import random
nums = []

for i in range(1,1001):
    nums.append(random.randint(10,99))

print(nums)
print(len(nums))
