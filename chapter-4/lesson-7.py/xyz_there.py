word = input("Input a word: ")

i = 0
found = False

while i < len(word) - 2:  
    if word[i:i+3] == "xyz" and (i == 0 or word[i-1] != '.'):
        found = True
        break
    i += 1

print(found)
