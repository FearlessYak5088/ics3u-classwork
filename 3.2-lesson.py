### If, Elif, Else
team_a_points = 25
team_a_wins = 15

team_b_points = 20
team_b_wins = 16

if team_a_points > team_b_points:
    print("Team A wins!")
    team_a_wins += 1
elif team_b_points > team_a_points:
    print("Team B wins!")
    team_b_wins += 1
else:
    print("Tie.")

if team_a_wins > team_b_wins:
    print("Team A has more wins than Team B.")
elif team_b_wins > team_a_wins:
    print("Team B has more wins than Team A.")
else:
    print("Both Teams A and B have the same number of wins.")
  
# Why do you suppose the output says "Both Teams A and B have the same number of wins." 
# when team_a_wins is initialized as only 15 and team_b_wins is initialized as 16? It seems Team B has more wins. What is going on?
"Throughout the program, Team A and B will gain wins, and the else statement is used when Team A or B does not have more wins that the other."

# What do you think elif and else are doing? Answer in a comment.
"elif is making the code run differently when the situation is different from the if code. Else makes the code run differently when the situation is not in any of the mentioned if or elif statements.

# Pick one of the elif statements and change it to if instead. What difference does that make? Why? Answer in a comment.
if team_b_points > team_a_points:
    print("Team B wins!")
    team_b_wins += 1
"This changes the code because now the else statement under it only pertains to the new if statement. Now, when Team B does not have more points that team A, it will say it is a Tie"

### How Old Are You, Specifically?
age = int(input("How old are you? "))
if age < 16: 
    print("You can't drive.")
elif ((age>= 16) and (age<= 17)): 
    print("You can drive but not vote.")
elif ((age>= 18) and (age<=20)):
    print("You can vote but not rent a car.")
else: 
    print("You can do pretty much anything.")

### Space Boxing
weight = float(input("please input your current weight in lbs: "))
print("""I have information on the following planets:
      1. Venus  2. Mars   3. Jupiter
      4. Saturn 5. Uranus 6. Neptune""")
planet = input("what planet are you visiting? ")

if (planet == "Venus" or planet == "1"):
  print(f"Your weight would be {weight * 0.78} lbs on Venus")
elif (planet == "Mars" or planet == "2"):
  print(f"Your weight would be {weight * 0.39} lbs on Mars")
elif (planet == "Jupiter" or planet == "3"):
  print(f"Your weight would be {weight * 2.65} lbs on Jupiter")
elif (planet == "Saturn" or planet == "4"):
  print(f"Your weight would be {weight * 1.17} lbs on Saturn")
elif (planet == "Uranus" or planet == "5"):
  print(f"Your weight would be {weight * 1.05} lbs on Uranus")
elif (planet == "Neptune" or planet == "6"):
  print(f"Your weight would be {weight * 1.23} lbs on Neptune")
else:
  print("Please enter a planet number or name.")

### A Little Quiz
right_answers = 0
input("Are you ready for a quiz? ")
print("Okay, here it comes")
answer_1 = int(input("""Q1) What is the capital of Alaska?
                        1) Melbourne
                        2) Anchorage
                        3) Juneau
                        """))
if answer_1 == 3:
    print("Correct")
    right_answers = right_answers + 1
elif answer_1 == 2 or answer_1 == 1:
    print("Incorrect")
else:
    print("Please input a number from 1-3")

answer_2 = int(input("""Q2)In Python, the way you get keyboard input is the keyobard_input function.
	                    1) true
	                    2) false
                        """))
if answer_2 == 2:
    print("Correct")
    right_answers = right_answers + 1
elif answer_2 == 1:
    print("Incorrect")
else:
    print("Please input a number from 1-2")

answer_3 = int(input("""Q3) What is the result of 9 + 6 / 3? 
                        1) 5
                        2) 11
                        3) 15/3
                        """))
if answer_3 == 2:
    print("Correct")
    right_answers = right_answers + 1
elif answer_3 == 1 or answer_3 == 3:
    print("Incorrect")
else:
    print("Please input a number from 1-3")
 
print(f"Overall, you got {right_answers}/3 correct. Thanks for playing")

