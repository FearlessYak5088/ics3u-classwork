def number_to_percent(x: float) -> int:
    percent = (x * 100)
    return print(round(percent))
    """ 
    This function converts a float between 0.0 to 1.0 into a percentage

    Args:
        x (float): Number between 0.0 and 1.0

    Returns:
        percent (int): Number converted to percent, without decimals
    
    """

def main():
    while True:
        try:
            x = float(input("Input a number from 0.0 to 1.0, I will turn it into a percentage. "))
            if x < 0.0 or x > 1.0:
                raise ValueError
            break
        except ValueError:
            print("Invalid number.")
    
    number_to_percent(x)


if __name__ == "__main__":
    main()


