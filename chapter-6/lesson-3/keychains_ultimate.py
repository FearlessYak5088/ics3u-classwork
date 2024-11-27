# Keychains for Sale, real ultimate power

def main():
    tax = 1.13
    base_shipping = 5.00
    per_keychain_shipping = 1.00
    keychains = 0
    keychain_price = 10.00
    while True:

        choice = int(input("""Ye Olde Keychain Shoppe

                1. Add Keychains to Order
                2. Remove Keychains from Order
                3. View Current Order
                4. Checkout

                Please enter your choice: """))
        if choice == 1:
            keychains = add_keychains(keychains)
        elif choice == 2:
            keychains = remove_keychains(keychains)
        elif choice == 3:
            view_order(keychains, keychain_price, tax, base_shipping, per_keychain_shipping)
        elif choice == 4:
            checkout(keychains, keychain_price, tax, base_shipping, per_keychain_shipping)
            break

def add_keychains(keychains: int) -> int:
    added_keychains = int(input(f"\nYou have {keychains} keychains. How many to add? "))
    keychains += added_keychains 
    print(f"You now have {keychains} keychains\n")
    return keychains

def remove_keychains(keychains: int) -> int:
    removed_keychains = int(input(f"\nYou have {keychains} keychains. How many to remove? "))
    while removed_keychains > keychains:
        print(f"Keychains can't be less than 0. Try again.")
        removed_keychains = int(input(f"\nYou have {keychains} keychains. How many to remove? "))
    else:
        keychains -= removed_keychains
        print(f"You now have {keychains} keychains\n")
    return keychains
    
def view_order(keychains: int, keychain_price: int, tax:int, base_shipping:int, per_keychain_shipping:int) -> None:
    if keychains > 0:
        subtotal = keychains * keychain_price 
        shipping_cost = (keychains * per_keychain_shipping) + base_shipping
        total_price = (subtotal + shipping_cost) * tax
        print(f"You have {keychains} keychains.\nKeychains cost ${keychain_price} each.\nSubtotal is {subtotal}\nShipping cost is {shipping_cost}\nTotal after tax is {total_price}\n")
    else:
        print("You have 0 keychains.")

def checkout(keychains: int, keychain_price: int, tax:int, base_shipping:int, per_keychain_shipping:int) -> None:
    name = input("What is your name? ")
    view_order(keychains, keychain_price, tax, base_shipping, per_keychain_shipping)
    print(f"Thank you for your order, {name}!")


if __name__ == "__main__":
    main()
