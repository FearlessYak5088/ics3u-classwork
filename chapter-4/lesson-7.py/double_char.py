word = input("Input a word: ")
char = ""

for i in range(len(word)):
    char += word[i] * 2

print(char)
