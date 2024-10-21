message = input("What is your message? ")

print()
print(f"Your message is {len(message)} characters long.")
print(f"The first character is at position 0 and is '{message[0]}'.")
lastpos = len(message) - 1
print(f"The last character is at position {lastpos} and is '{message[lastpos]}'.")
print()
print("Here are all the characters, one at a time:\n")

for i in range(len(message)):
    print(f"\t{i} - '{message[i]}'")

a_count = 0
for i in range(len(message)):
    letter = message[i].lower()
    if letter == 'a':
        a_count += 1

print(f"\nYour message contains the letter 'a' {a_count} times.")

If you print range(7), what do you see? What happens if you convert the range to a list and then print that out? E.g., list(range(7))
If you print range(7), it will only count the first 7 characters (index 0 to 6)

The for loop is defined so that the loop variable i iterates through the entire range object range(len(message)). If the message was "Hello" what number would be sent to the range function? What numbers would be included within that range object? List them out.
The number 5 would be sent because its length is 5. The numbers 0-4 would be included in the range. Indices start at 0 for the first character.
  
If a string variable contains the value "box", what is its length? What is the index (position) of the last character (the 'x')?
The length is 3, the index of x is 2. 

Currently the code prints out the number of ‘a’s in the message. Change it so that it instead prints out the number of vowels (a A e E i I o O u U).

vowel_count = 0
vowel = ["a", "e", "i", "o", "u"]

for i in range(len(message)):
    letter = message[i].lower()
    if letter in vowel:
        vowel_count += 1

print(f"\nYour message contains {vowel_count} vowels.")
