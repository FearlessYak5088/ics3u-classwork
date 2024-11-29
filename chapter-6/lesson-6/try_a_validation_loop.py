def main():
    while True:
        try:
            age = int(input("Please enter your age: "))
            break
        except ValueError:
            print("Need to input an integer!\n")
    print(f"Wow, you are {age} years old.")


if __name__ == "__main__":
    main()

# What is the error that happens when you try to convert a string that cannot be converted to an integer?
# Value Error

# Use that error in the except section.
# Purposefully enter invalid input to see how the program handles the error.
# Why doesn’t the loop break right after taking the input?
# Inputting the wrong value causes the except line to be executed, printing another line, continuing the code.
