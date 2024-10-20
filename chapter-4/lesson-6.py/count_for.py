print("Type in a message, and I'll display it five times.")

message = input("Message: ")

for n in range(0, 5, 1):
    print(f"{n}. {message}")

# What happens when you change the loop variable n to some other name?(Then change it back.) Why do you suppose I chose to name this particular loop variable “n”?
# Nothing happens when the loop variable is renamed. The variabled "n" was chosen because it is always used when representing numbers. 

# How do the first two arguments (0, 5) given to the range function effect the loop? Change them and experiment. Change it back.
# It makes it count from 0 up to but not including 5. 

# What do you suppose the third number given to the range function is for? Change it to 2 and see. Change it back.
# It is the how much the it counts up by in the range. Ex. if its 1, it counts everyone number in the range. If its 2, it counts every second number in the range.

# What happens when you call the range function with only one number? i.e. range(7)?
# It counts from 0 until the number before the number you put in. 

# What happens when you call the range function with only two numbers? i.e. range(3, 9)?
# It starts from the first number, and ends at the number before the last number. 

# Change the code so that the loop repeats ten times instead of five.
print("Type in a message, and I'll display it ten times.")

message = input("Message: ")

for n in range(10):
    print(f"{n}. {message}")


See if you can change the for loop so that the message starts at 2 and counts by twos
print("Type in a message, and I'll display it ten times.")

message = input("Message: ")

for n in range(2, 22, 2):
    print(f"{n}. {message}")
