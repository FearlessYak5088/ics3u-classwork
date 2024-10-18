import math

while True:
    number = int(input("Enter a number: "))
    if number > 0:
        print(f"The square root of {number} is {math.sqrt(number)}")
        break
    elif number < 0: 
        print("You can't take the square root of a negative number.")
        continue
