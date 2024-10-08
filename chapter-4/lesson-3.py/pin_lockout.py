PIN = "12345"
tries = 0

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")
tries += 1

while entry != PIN and tries < 3:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")
    tries += 1

if entry == PIN:
    print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")
elif tries >= 3:
    print("\nYOU HAVE RUN OUT OF TRIES. ACCOUNT LOCKED.")

# Change the code so that it locks them out after 4 tries instead of 3. Make sure to change the condition at the bottom, too.
while entry != PIN and tries < 4: 
elif tries >= 4:

# Make a variable (constant) for the number of maximum tries allowed. Use that variable everywhere instead of just the number.
PIN = "12345"
tries = 0
maxtries = 4

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")
tries += 1

while entry != PIN and tries < maxtries:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")
    tries += 1

if entry == PIN:
    print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")
elif tries == maxtries:
    print("\nYOU HAVE RUN OUT OF TRIES. ACCOUNT LOCKED.")
