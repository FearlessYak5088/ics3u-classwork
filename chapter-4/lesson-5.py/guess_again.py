import random

number = random.randint(1,10)
guess = int(input("I have chosen a number from 1 to 10. Try to guess it\n"))
count = 1

while True:
    count += 1
    if guess!= number:
        guess = int(input("Incorrect. Guess again.\n"))
    if guess == number:
        print(f"That's right! It took you {count} tries")
        break
