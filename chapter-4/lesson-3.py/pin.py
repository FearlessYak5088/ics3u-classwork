PIN = "12345"

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")

while entry != PIN:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")


print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")

# How is a while loop similar to an if statement?
# Both while loops and if statements will function if their requirements are met. 

# How is a while loop different from an if statement?
# While loops will repeating the same program as long as it still meets its requirements. If statements only run once.

# What would we have to change in our program if the PIN was stored as an integer rather than a string? For example if it was initialized as PIN = 12345.
# the entry line would have the int() function because we are now working with integers. The new code would be:
PIN = 12345

print("WELCOME TO THE BANK OF GALLO.")
entry = int(input("ENTER YOUR PIN: "))

while entry != PIN:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = int(input("ENTER YOUR PIN: "))

# Comment out the line entry = input(...) from inside the while loop. What happens? Why?
# It will keep printing "INCORRECT PIN. TRY AGAIN." when the entered pin is wrong because the user is not able to change their pin, making it forever incorrect.
  
# (Uncomment the entry = input(...) before you turn in the assignment.)
