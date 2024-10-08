import random

number = random.randint(1,10)
guess = int(input("I have chosen a numer between 1 and 10. Try to guess it.\nYour guess: "))

while guess != number:
  guess = int(input("Incorrect. Guess again: "))
if guess == number:
  print("Correct!")
