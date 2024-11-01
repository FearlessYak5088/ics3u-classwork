print("I have a class of 33 students.")
print("There are 11 girls, so that means..")
# Subtract the total number of students by the number of girls to get the total number of boys
print("there are " + str(33 - 11) + " boys.")
print()
# Divide the number of girls by the number of students to get the percentage of girls
print(f"That means {11 / 33} % are girls...")
print(f"That means {round(11 / 33, 2)} % are girls...")
# Divide the number of boys by the number of students to get the percentage of boys
print(f"and {((33 - 11) / 33)} % are boys.")
print(f"and {round((33-11) / 33, 2)} % are boys.")
print()
print("If we made groups of six...")
# Divide the number of students by six to make six even groups
print(f"There would be {33 // 6} groups of six.")
# Get the remainder by using the modulus 
print(f"And then a smaller group of {33 % 6} people.")
# Print the hyphen sign thirty times to draw a line
print("-" * 30)
print("If we had 17 apples and 3 people...")
# Divide seventeen apples by three people to get the number of apples per person
print(f"Each person would get {17 // 3} whole apples.")
# Get the remaining apples by using the modulus operator
print("There would be " + str(17 % 3) + " apples remaining.")
print()
print("If we charged each person $2 each for their 5 apples..")
# Multiply two by five apples to get the amount that each person would pay
print("they would each pay ${}.".format(2 * 5))
