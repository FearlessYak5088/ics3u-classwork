# Keychains for Sale, for real this time

def main():
    while True:
        keychains = 0
        keychain_price = 10

        choice = int(input("""Ye Olde Keychain Shoppe

                1. Add Keychains to Order
                2. Remove Keychains from Order
                3. View Current Order
                4. Checkout

                Please enter your choice: """))
        if choice == 1:
            add_keychains(keychains)
        elif choice == 2:
            remove_keychains(keychains)
        elif choice == 3:
            view_order(keychains, keychain_price)
        elif choice == 4:
            checkout(keychains, keychain_price)

def add_keychains(keychains: int) -> int:
    added_keychains = int(input(f"\nYou have {keychains} keychains. How many to add? "))
    keychains += added_keychains 
    result = print(f"You now have {keychains} keychains\n")
    return result
def remove_keychains(keychains: int) -> int:
    removed_keychains = int(input(f"\nYou have {keychains} keychains. How many to remove? "))
    keychains -= removed_keychains
    result = print(f"You now have {keychains} keychains\n")
    return result
def view_order(keychains: int, keychain_price: int) -> None:
    total_price = keychains * keychain_price
    result = print(f"You have {keychains} keychains.\nKeychains cost ${keychain_price} each.\nTotal price is {total_price}\n")
    return result
def checkout(keychains: int, keychain_price: int) -> None:
    total_price = keychains * keychain_price
    name = input("What is your name? ")
    result = print(f"You have{keychains} keychains.\nKeychains cost ${keychain_price} each.\nTotal price is {total_price}.\nThank you for your order, {name}!")
    return result
    quit


if __name__ == "__main__":
    main()
