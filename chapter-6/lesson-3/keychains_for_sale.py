# Keychains for Sale

def add_keychains():
    return print("\nADD KEYCHAINS\n")
def remove_keychains():
    return print("\nREMOVE KEYCHAINS\n")
def view_order():
    return print("\nVIEW ORDER\n")
def checkout():
    return print("\nCHECKOUT\n")
    quit

def main():
    while True:
        choice = int(input("""Ye Olde Keychain Shoppe

        1. Add Keychains to Order
        2. Remove Keychains from Order
        3. View Current Order
        4. Checkout

        Please enter your choice: """))
        if choice == 1:
            add_keychains()
        elif choice == 2:
            remove_keychains()
        elif choice == 3:
            view_order()
        elif choice == 4:
            checkout()

if __name__ == "__main__":
    main()
