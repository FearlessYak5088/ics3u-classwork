### Twenty Questions… well, actually just Two

answer1 = input("Question 1) Is it animal, vegetable, or mineral? ").lower()
answer2 = input("Question 2) Is it bigger than a breadbox? (yes/no) ").lower() 

if answer2 == "yes": 
    bigger = True 

    if answer1 == "animal": 
        if bigger == True:
            print("It's a moose")
        else:
            print("It's a squirrel")

    elif answer1 == "vegetable": 
        if bigger == True:
            print("It's a watermelon")
        else:
            print("It's a carrot")

    elif answer1 == "mineral":
        if bigger == True:
            print("It's a Camaro")
        else:
            print("It's a paper clip")
            
else:
    print("Please choose animal, vegetable, or mineral.")

### Choose your own adventure
choice1 = input("""You are in room 1. Would you like to go to kitchen or upstairs? (kitchen/upstairs)
                > """)
if choice1 == "kitchen":
    choice2 = input("""You are in the kitchen. Would you like to open the fridge or cabinet? (fridge/cabinet)
                    > """)
    if choice2 == "fridge":
        choice3 = input("""Inside the fridge there is myserious looking milk and cake. Which one will you eat? (milk/cake) 
                        > """)
        if choice3 == "milk":
            print("The milk you drank was poisoned. You become nauseous and die")
        elif choice3 == "meat":
            print("The cake you ate turned out to be high quality German chocolate cake. You enjoy the dessert")
    elif choice2 == "cabinet":
        choice3 = input("""Inside the cabinet there are crackers and a bag of sugar. Which one will you choose? (crackers/sugar) 
                        > """)
        if choice3 == "crackers":
            print("You eat the crackers. A nice dry snack")
        elif choice3 == "sugar":
            print("The bag of sugar is so addicting (it's laced). You overdose on powder sugar")
    elif choice2 == "cabinet":
        choice3 = input(" ")
elif choice1 == "upstairs":
    choice2 = input("""You are upstairs. Would you like to go to the bedroom or bathroom? (bedroom/bathroom)
                    > """)
    if choice2 == "bedroom":
        choice3 = input("""You are in the bedroom. Would you like to open the closet or sleep in the bed? (closet/sleep)
                        > """)
        if choice3 == "closet":
            print("A scary man comes out of the closet and stabs you")
        elif choice3 == "sleep":
            print("You get a good night's sleep")
    elif choice2 == "bathroom":
            choice3 = input("""You are in the bathroom. Would you like to pull back the shower curtain or use the toilet? (curtain/toilet)
                            > """)
            if choice3 == "curtain":
                print("Someone is behind the shower curtain and stabs you")
            elif choice3 == "toilet":
                print("You relieve yourself with a nice relaxing time on the porcelain throne")

### Age Messages 3
age = int(input("How old are you? "))

if age < 16:
    print("You can't drive")
if age >= 16:
    if age == 16 or age == 17: 
        print("You can drive but not vote")
    if age >=18 and age <=24:
        print("You can vote but not rent a car")
    if age >= 25:
        print("You can do pretty much anything")

### Two More Questions
print("think of an object and I will guess it")
location = input("Question 1) Is it inside, outside, or both? (inside/outside/both) ").lower()
alive = input("Question 2) Is it alive? (yes/no) ").lower()

if location == "inside" and alive == "yes":
    print("It's a houseplant")
if location == "inside" and alive == "no":
    print("It's a shower curtain")
if location == "outside" and alive == "yes":
    print("It's a bison")
if location == "outside" and alive == "no":
    print("It's a billboard")
if location == "both" and alive == "yes":
    print("It's a dog")
if location == "both" and alive == "no":
    print("It's a cell phone")
    
### BMI Categories
feet = int(input("Enter height (feet only): "))
inches = int(input("Enter height (inches): "))

total_inches = (feet * 12) + inches
height_m = total_inches * 0.0254

weight_lbs = float(input("Enter weight (pounds): "))

weight_kg = weight_lbs * 0.45359237

bmi = weight_kg / (height_m ** 2)

if bmi < 18.5:
    category = "underweight"
if bmi >= 18.5 and bmi <= 24.9:
    category = "normal weight"
if bmi >= 25.0 and bmi <=  29.9:
    category = "overweight"
if bmi > 30.0:
    category = "obese"

print(f"The BMI is {bmi}, which is {category}")

### Gender Game
gender = input("What is your gender? (M or F): ").lower()
first_name = input("First Name: ")
last_name = input("Last Name: ")
age = int(input("Age: "))

if gender == "F".lower(): 
    if age >= 20:
        marry = input(f"Are you married, {first_name}? (Y or N) ").lower()
        if marry == "Y".lower():
            print(f"I will call you Mrs. {last_name}")
        elif marry == "N".lower():
            print(f"I will call you Ms. {last_name}")
    else:
        print(f"I will call you {first_name + " " + last_name}")
if gender == "M".lower():
    if age >= 20:
        print(f"I will call you Mr. {last_name}")
    else:
        print(f"I will call you {first_name + " " + last_name}")
### Alpha Order
# Examples where the first word comes before the second word
print(f"'apple' comes before 'banana': {'apple' < 'banana'}")
print(f"'cat' comes before 'dog': {'cat' < 'dog'}")
print(f"'ant' comes before 'bear': {'ant' < 'bear'}")
print(f"'blue' comes before 'green': {'blue' < 'green'}")
print(f"'car' comes before 'doghouse': {'car' < 'doghouse'}")

# Examples where the first word comes after the second word
print(f"'zebra' comes after 'apple': {'zebra' > 'apple'}")
print(f"'xylophone' comes after 'violin': {'xylophone' > 'violin'}")
print(f"'sun' comes after 'moon': {'sun' > 'moon'}")
print(f"'yellow' comes after 'red': {'yellow' > 'red'}")
print(f"'queen' comes after 'knight': {'queen' > 'knight'}")

### Attendance
last_name = input("What is your last name? ")

if last_name[0].lower() <= 'd':
    print(f"You last name is {last_name}. You will be called early")
elif 'e' <= last_name[0].lower() <= 'k':
    print(f"Your last name is {last_name}. You'll be called in the middle of roll call.")
elif 'l' <= last_name[0].lower() <= 'r':
    print(f"Your last name is {last_name}. You'll be called later during roll call.")
else:
    print(f"Your last name is {last_name}. You'll be called last in roll call.")

### The Worst Guessing Game Ever
number = 2
guess = int(input("I'm thinking of a whole number from 1-10. Try to guess it. "))

if guess == number:
    print("You got it!")
elif guess < 1 or guess > 10:
    print("Please enter a valid number")
else:
    print("Wrong number")


