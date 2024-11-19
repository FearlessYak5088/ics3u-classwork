import random
import os
import time


def main():
    for i in range(100000):
        r = random.randrange(1, 6)
        if r == 1:
            first()
        elif r == 2:
            second()
        elif r == 3:
            third()
        elif r == 4:
            fourth()
        elif r == 5:
            fifth()

        time.sleep(0.02)  
        
        os.system("cls")  # clear console

    print("I pledge allegiance to the flag.");


def first():
    print("I                               ");


def second():
    print("  pledge                        ");


def third():
    print("         allegiance             ");


def fourth():
    print("                    to the      ");


def fifth():
    print("                           flag.");


if __name__ == "__main__":
    main()
