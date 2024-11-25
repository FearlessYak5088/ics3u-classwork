# 1. Given the code below, answer the following questions:
# How many arguments are sent to the num_chairs function? What are they?
# 2 arguements (4, 5)

# What are the names of the parameter variables? What values are they assigned from running the code below?
# tables, chairs. They are assigned values 4 for tables, and 5 for chairs_per_tables.

# What is the output?
# You will need 20 chairs.

# What happens when you remove an argument? when you add one?
# The code does not run

def num_chairs(tables, chairs_per_table):
    chairs = tables * chairs_per_table
    print(f"You will need {chairs} chairs.")


num_chairs(4, 5)


# 2. Create a function that takes one integer argument and simply prints it out. Call this function print_integer.
def print_integer(x):
    print(x)

print_integer(12)

# 3. Create a function that takes two integer arguments and prints out their difference. You can use math.abs() for absolute value.
import math

def integer_difference(x:int, y:int) -> int:
    difference = abs(x - y)
    print(difference)

integer_difference(10,7)

# 4. List the two things wrong with the following code and how to fix it.
function subtract(a):
    print(a - b)

subtract(5, 7)

# There is only 1 parameter while there are 2 arguements, and the functions only prints the arguements rather than subtracting them.
# Fixed code
function subtract(a, b):
    difference = abs(a-b)
    print(difference)

subtract(5, 7)
# 5. How would you call the following function? Give two examples.
def activate_thrusters(percent_power):
    pass

# The function name and the arguement in brackets
activate_thrusters(50)

# 6. What is wrong with how the code below calls a function that takes a name and how many apples that person will eat? 
person_apples
# Give an example of the correct way to do it.
function_name(person, apples)

