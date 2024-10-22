word = input("input a word: ")

i = 0
bob = False

while i < len(word) - 2:
    if word[i].lower() == "b" and word[i+2].lower() == "b":
        bob = True
        break 
    i += 1
    
print(bob)
