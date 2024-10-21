word_1 = input("Input a word: ").lower()
word_2 = input("Input a second word: ").lower()

if word_1[-len(word_2):] == word_2 or word_2[-len(word_1):] == word_1:
    print(True)
else:
    print(False)
