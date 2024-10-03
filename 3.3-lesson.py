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
