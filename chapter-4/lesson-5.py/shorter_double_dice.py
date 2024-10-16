### Original
import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

while dice1 != dice2:
  print(f"\nRoll #1: {dice1}\nRoll #2: {dice2}\nThe total is {dice1 + dice2}!")
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
if dice1 == dice2:
  print(f"\nRoll #1: {dice1}\nRoll #2: {dice2}\nThe total is {dice1 + dice2}! Both dice are the same number.")

### While True Break Loop
import random

while True:
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  print(f"\nRoll #1: {dice1}\nRoll #2: {dice2}\nThe total is {dice1 + dice2}!")
  if dice1 == dice2:
    print(f"\nRoll #1: {dice1}\nRoll #2: {dice2}\nThe total is {dice1 + dice2}! Both dice are the same number.")
    break
