# Create a program that will read in wins losses and ties from a single string variable (shown below). 
# The goal is to convert those outcomes to point values
# Win - 2, Tie - 1, Loss - 0.
# W W L T T W
# Should get a list of points as follows: [2, 2, 0, 1, 1, 2]

string = "W W L T T W"

string_int = string.split(" ")

list = []

for string in string_int:
    if string == "W":
        list.append(2)
    elif string == "L":
        list.append(0)
    else:
        list.append(1)

print(list)

