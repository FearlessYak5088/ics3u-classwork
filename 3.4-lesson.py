### Randomness
# What happens if we change random.randrange(1, 6) to random.randrange(1, 5)? 
# Make the change and run the program a few times to see the result. What seems to be the new range of numbers that pop up?

# Numbers ranging 1 and 4


# After the import statement, use the random.seed() function and give it an integer like random.seed(400). What do you notice? 
# What happened to the random numbers?

# They all follow the same sequence every time the program runs


# Change to random seed to something else and observe the behavior. What happens to the random numbers?

# They follow the new randomly generated sequence


# There are a couple popular games I can think of that use this concept of a “seed”. 
# Why do you suppose they use it and what does it do in the game?

# Games use seeds for generating levels or worlds, making sure that every time they generate a specific seed, it always is the same content

### Magic 8-Ball
import random

input("What do you have to ask the Magic 8-Ball? ")

choice = random.randrange(1, 21)  
response = ""

if choice == 1:
    response = "It is certain"
elif choice == 2:
    response = "It is decidedly so"
elif choice == 3:
    response = "Without a doubt"
elif choice == 4:
    response = "Yes - definitely"
elif choice == 5:
    response = "You may rely on it"
elif choice == 6:
    response = "As I see it, yes"
elif choice == 7:
    response = "Most likely"
elif choice == 8:
    response = "Outlook good"
elif choice == 9:
    response = "Signs point to yes"
elif choice == 10:
    response = "Yes"
elif choice == 11:
    response = "Reply hazy, try again"
elif choice == 12:
    response = "Ask again later"
elif choice == 13:
    response = "Better not tell you now"
elif choice == 14:
    response = "Cannot predict now"
elif choice == 15:
    response = "Concentrate and ask again"
elif choice == 16:
    response = "Don't count on it"
elif choice == 17:
    response = "My reply is no"
elif choice == 18:
    repsonse = "My sources say no"
elif choice == 19:
    response = "Outlook not so good"
elif choice == 20:
    response = "Very doubtful"
else:
    response = "8-BALL ERROR!"

print("MAGIC 8-BALL SAYS: " + response)

### A Number Guessing Game
import random
number = random.randrange(1, 11)
guess = int(input("I am thinking of a number from 1 to 10. Guess the number: "))
if guess == number:
    print(f"Correct! I was thinking of {number}!")
if guess != number:
    print(f"Incorrect. I was thinking of {number}")
if guess < 1 or guess > 10:
    print("Please input a number from 1 to 10.")

### Fortune Cookie
import random
fortune = random.randint(1, 6)
lottery = random.randrange

num1 = random.randint(1, 54)
num2 = random.randint(1, 54)
num3 = random.randint(1, 54)
num4 = random.randint(1, 54)
num5 = random.randint(1, 54)
num6 = random.randint(1, 54)

while len({num1, num2, num3, num4, num5, num6}) < 6:
    num1 = random.randint(1, 54)
    num2 = random.randint(1, 54)
    num3 = random.randint(1, 54)
    num4 = random.randint(1, 54)
    num5 = random.randint(1, 54)
    num6 = random.randint(1, 54)

if fortune >= 1 or fortune >= 6:
    if fortune == 1:
        print("A bold decision you make soon will lead to unexpected rewards.")
    if fortune == 2:
        print("An exciting opportunity is waiting for you; stay open to new possibilities.")
    if fortune == 3:
        print("Your determination will turn a challenge into a great success.")
    if fortune == 4:
        print("Someone from your past will bring you good news soon.")
    if fortune == 5:
        print("Trust your instincts-they will guide you to the right path.")
    if fortune == 6:
        print("Your creativity will open doors to new adventures and connections.")
    print(f"Lottery numbers:{num1, num2, num3, num4, num5, num6} ")

### Dice
import random
roll1 = random.randint(1,6)
roll2 = random.randint(1,6)

print(f"Roll 1: {roll1} \nRoll 2: {roll2} \nTotal: {roll1 + roll2}")

### One Shot Hi-Lo
import random

secret_number = random.randint(1,100)

guess = int(input("I'm thinking of a number from 1-100. Try to guess it. \n"))

if 1 <= guess <=100:
    if guess == secret_number:
        print("You guessed it! That was a 1 percent chance!")
    elif guess > secret_number:
        print(f"Incorrect. Your guess is too high. The number is {secret_number}.")
    elif guess < secret_number:
        print(f"Incorrect. Your guess is too low. The number is {secret_number}.")
else:
    print("Please input a number from 1-100.")

### Three Card Monte
import random

ace = random.randint(1,3)

print("You slide up to Fast Eddie's card table and plop down your cash. \nHe glances at you out of the corner of his eye and starts shuffling. \nHe lays down three cards.")

guess = int(input("""Which one is the ace?
                        ##  ##  ##
                        ##  ##  ##
                        1   2   3
                        """))

if guess == ace:
    print("You nailed it! Fast Eddie reluctantly hands over your winnings, scowling.")
elif guess != ace and 1 <= guess <= 3:
    print(f"Ha! Fast Eddie wins again! The ace was card number {ace}.")
else:
    print("You have to guess one of the three cups...")
