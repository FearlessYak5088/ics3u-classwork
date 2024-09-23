# More Variables and Printing

store = "No Frills"
item = "Apples"
price = 0.5
quantity = 7
subtotal = price * quantity
tax = subtotal * 0.05
total = tax + subtotal

# f-string
print(f"At {store} I bought some {item}.")

# concatenation
print("They sold for $" + str(price) + " each.")

# dot format
print("I wanted to purchase {} of them.".format(quantity))

# f-string
print("The total price, with tax included, was ${total}.")


1. You will notice that the last line of output doesn’t actually inject the total value into the string. What is missing in that line that is present in the first print line?
# It is missing the 'f' before the string. There are curly brackets, but there is nothing to format the string. The correct line would be:
print(f"The total price, with tax included, was ${total}.")

2. Above each print function call, write a comment telling me which formatting approach was used.
  f-string
  “dot format”
  concatenation

3. Before the last line of output, include some output message(s) describing the subtotal and the tax amounts.
print(f"The subtotal before tax was ${round(subtotal, 2)}.")
print(f"The tax amount was ${round(tax, 2)}.")

4. Change some of the variable values and observe how they alter the running of the program.

# Changes
store = "Food Basics"
item = "Bananas"
price = 0.45
quantity = 9
subtotal = price * quantity
tax = subtotal * 0.05
total = tax + subtotal

print(f"At {store} I bought some {item}.")
print("They sold for $" + str(price) + " each.")
print("I wanted to purchase {} of them.".format(quantity))
print(f"The subtotal before tax was ${round(subtotal, 2)}.")
print(f"The tax amount was ${round(tax, 2)}.")
print(f"The total price, with tax included, was ${total}.")

# Results
At Food Basics I bought some Bananas.
They sold for $0.45 each.
I wanted to purchase 9 of them.
The subtotal before tax was $4.05.
The tax amount was $0.2.
The total price, with tax included, was $4.2524999999999995.
  
