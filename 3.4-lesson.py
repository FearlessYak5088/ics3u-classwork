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

