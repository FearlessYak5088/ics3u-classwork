# Hello, Name!
def main():
    name = input("Enter your name: ")

    if name == "":
        name = "User"
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()

# Area Calculator
def greet():
    print("Welcome to the awesome area calculator!")
    print()

if __name__ == "__main__":
    greet()
    
length = int(input("Enter a length: "))
width = int(input("Enter a width: "))
print()

area = length * width

print(f"The area is {area} units squared")

# Ticket Prices
TICKET_PRICE = 13.95
def main():
    num_tickets = int(input("How many tickets would you like? "))
    total_price = num_tickets * TICKET_PRICE
    print(f"The total price is {total_price}")

if __name__ == "__main__":
    main()
