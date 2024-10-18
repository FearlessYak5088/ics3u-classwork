import math

print("Enter three integers")
side_1 = int(input("Side 1: "))
side_2 = int(input("Side 2: "))

while True:
    if side_2 < side_1:
        print(f"{side_2} is smaller than {side_1}. Try again")
        side_2 = int(input("Side 2: "))
        continue
    elif side_2 >= side_1: 
        side_3 = int(input("Side 3: "))
        print(f"Your three sides are {side_1} {side_2} {side_3}")
        if side_1**2 + side_2**2 == side_3**2:
            print("These sides make a right triangle.")
            break
        else:
            print("These sides do not make a right triangle.")
            break
