# User Input
# 1. The price has a float function, and the input is on a single line
# 2. 
name = input("The name of the item:")

price = float(input("The price: $"))

print("How many do you want?")
quantity = int(input())

subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print()
print(f"You choose to buy {quantity} {name}.")
print(f"That will come out to ${total}")
