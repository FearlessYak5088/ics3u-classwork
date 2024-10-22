string1 = input("input the first string: ")
string2 = input("input the second string: ")

i = 0
string3 = ""

while i < len(string1) or i < len(string2):
    if i < len(string1):
        string3 += string1[i] 
    if i < len(string2):
        string3 += string2[i] 
    i += 1  

print(string3)
