# Create a program that will split a string of integers separated by comma-space. 
# For example "65, 75, 32, 22". Be sure to convert the numbers to integers. Print out all the index locations matched with the values.

string = "65, 75, 32, 22"

list = []

string_int = string.split(" ")
string_int = string.split (",")

for string in string_int:
    list.append(int(string))
for i in range(len(list)):
    print(f"{i}: {list[i]}")
