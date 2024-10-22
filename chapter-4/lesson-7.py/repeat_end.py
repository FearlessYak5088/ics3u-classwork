string = input("input a string: ")
integer = int(input("input an integer: "))

string2 = ""
i = 0

while i < len(string[-integer:]):
    if integer > 0:
        string2 += string[-integer:]
        i += 1
    elif integer <= 0:
        break

print(string2)
