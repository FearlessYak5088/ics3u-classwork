print("Type in a message, and I'll display it five times.")

message = input("Message: ")
print()

n = 0
while n < 5:
    print(f"{n + 1}. {message}")
    n += 1

# 1. What does n += 1 do? Remove it and see what happens. (Then put it back.) ctrl + c may come in handy.
  # n += 1 adds 1 to the value of n.
print("Type in a message, and I'll display it five times.")

message = input("Message: ")
print()

n = 0
while n < 5:
    print(f"{n + 1}. {message}")
  # When n + = 1 is removed, the program outputs "1. hi" forever. This happens because the value of n does not change, so it is forever less than 5, and forever in the while loop.
  
# 2. Change the code so that the loop repeats ten times instead of five.
print("Type in a message, and I'll display it ten times.")

message = input("Message: ")
print()

n = 0
while n < 10:
    print(f"{n + 1}. {message}")
    n += 1
  
# 3. See if you can change the code so that the message still prints ten times, but the numbers in front count by tens, like so:

Type in a message, and I'll display it ten times.
Message: I'm sending out an S.O.S.

10. I'm sending out an S.O.S.
20. I'm sending out an S.O.S.
30. I'm sending out an S.O.S.
40. I'm sending out an S.O.S.
50. I'm sending out an S.O.S.
60. I'm sending out an S.O.S.
70. I'm sending out an S.O.S.
80. I'm sending out an S.O.S.
90. I'm sending out an S.O.S.
100. I'm sending out an S.O.S.

print("Type in a message, and I'll display it ten times.")

message = input("Message: ")
print()

n = 0
while n < 100:
    print(f"{n + 10}. {message}")
    n += 10

# 4. Change the code so that it asks the person how many times to display the message. Then, print it that many times. Still count by tens.

Type in a message, and I'll display it several times.
Message: HELLO! My name is Inigo Montoya. You killed my father; prepare to die.

How many times? 3
10. HELLO! My name is Inigo Montoya. You killed my father; prepare to die.
20. HELLO! My name is Inigo Montoya. You killed my father; prepare to die.
30. HELLO! My name is Inigo Montoya. You killed my father; prepare to die.

print("Type in a message, and I'll display it ten times.")

message = input("Message: ")

amount = int(input("How many times? "))

print()

n = 0
while n < amount * 10:
    print(f"{n + 10}. {message}")
    n += 10
