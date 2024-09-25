# User Input
# 1. The price has a float function, and the input is on a single line
# 2. 
name = input("The name of the item: ")
quantity = int(input("How many do you want? "))
# 3. A prompt is the text before an input function, which usually tells the user what type of data they should input. The problem with the code is that the input function is before the text (the prompt), so the user will not know what to input
# 4. The int() and float() functions convert a string into an integer or floating-point number (with decimal). Without int() or float() the input will be treated as a string, and you wouldn't be able to perform calculations with it.


# The Forgetful Machine
# Ask for two words
input("Enter the first word: ")
input("Enter the second word: ")

# Ask for two numbers
input("Enter the first number: ")
input("Enter the second number: ")

print("Thanks for answering")


# Name, Age, and Salary
name = (input("Hello. What is your name? "))
age = (input(f"Hi, {name}! How old are you? "))
print(f"So you're {age} eh? That's not old at all!")
income = (input(f"How much do you make, {name}?"))
print(f"{income}! I hope that's per hour and not per year! LOL!")


# More User Input of Data
print("Please enter the following information so I can sell it for a profit!")
first_name = input("First name: ")
last_name = input("Last name: ")
grade = input("Grade (9-12): ")
student_id = input("Student-ID: ")
login = input("Login: ")
average = input("average: ")

print(f"\nYour information:\nFirst Name: {first_name:<20}\nLast Name: {last_name:<20}\nGrade: {grade:<20}\nStudent-ID: {student_id:<20}\nLogin: {login:<20}\nAverage: {average:<20}")


# Age in Five Years
name = input("Hello. What is your name? ")
age = int(input(f"Hi, {name}! How old are you? "))
age_minus_five = age - 5
age_plus_five = age + 5

print(f"Did you know that in five years you will be {age_plus_five} years old?")
print(f"And five years ago you were {age_minus_five}! Imagine that!")


# A Silly Calculator
numberone = float(input("What is your first number? "))
numbertwo = float(input("What is your second number? "))
numberthree = float(input("What is your third number? "))
answer = (numberone + numbertwo + numberthree) / 2

print(f"{numberone} + {numbertwo} + {numberthree} / 2 is ... {answer}")


# BMI Calculator
# Ask for height in feet and inches
feet = int(input("Enter height (feet only): "))
inches = int(input("Enter height (inches): "))

# Convert height to meters
total_inches = (feet * 12) + inches
height_m = total_inches * 0.0254

# Ask for weight in pounds
weight_lbs = float(input("Enter weight (pounds): "))

# Convert weight to kilograms
weight_kg = weight_lbs * 0.45359237

# Calculate BMI
bmi = weight_kg / (height_m ** 2)

# Display the result
print(f"The BMI is {bmi}")




