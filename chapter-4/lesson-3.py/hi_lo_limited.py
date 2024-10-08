import random

number = random.randint(1,100)
guess = int(input("I'm thinking of a random number from 1 to 100. You have 7 guesses.\nFirst Guess: "))
count = 1

while guess != number and count < 7:
  count += 1
  if guess > number:
    guess = int(input(f"Sorry, your guess is too high.\nGuess #{count}: "))
  elif guess < number:
    guess = int(input(f"Sorry, your guess is too low.\nGuess #{count}:"))
if guess != number and count == 7:
  print("Sorry, you didn't get it in 7 tries. You lost.")
elif guess == number:
  print("You guessed it!")
