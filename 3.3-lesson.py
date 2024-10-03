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

