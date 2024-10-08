import random

count = 0
number = random.randint(1,10)
guess = int(input("I have chosen a numer between 1 and 10. Try to guess it.\nYour guess: "))

while guess != number:
  guess = int(input("Incorrect. Guess again: "))
  count += 1
if guess == number:
  count += 1
  print(f"Correct! It took you {count} tries")
