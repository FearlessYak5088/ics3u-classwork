def main():
    item_price = -2.99
    quantity = 3
    print(f"{quantity} items at ${item_price} each is:")
    print(f"${calc_subtotal(item_price, quantity)}")


def calc_subtotal(price: float, quantity: int) -> float:
    """Calculate the subtotal for a single item in a cart.
    
    Args:
        price: The price of a single item.
        quantity: Number of a particular item in the cart.

    Returns:
        The subtotal
    """
    if price < 0:
        raise ValueError("Price cannot be negative.")

    return price * quantity


if __name__ == "__main__":
    main()


# In the main function, make the item_price a negative number. i.e., -2.99. Run the program and explain what happens. Answer the following in a comment.
# What is the error?
# Value Error

# What is the message?
# Price cannot be negative

# On what line does the error occur?
# Line 19

# What caused the error?
# item_price < 0.


# In the calc_subtotal function, add a check for the quantity value. Quantities cannot be negative so also raise a ValueError if the quantity is negative. 
# In the main function fix the item_price variable to make it positive and make the quantity negative to observe the error.
if quantity < 0:
    raise ValueError("Quantity cannot be negative")
  
  
# In the main function, make both item_price and quantity negative. What do you see and what do you not see. Explain in a comment.
# Only see the item_price Value Error, because it checks for it first, and does not continue going through the code.
