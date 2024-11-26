# Area calc
import math

def area_circle(radius: int) -> float:
    return math.pi * radius ** 2
def area_square(side: float) -> float:
    return side * side
def area_rectangle(length: float, width: float) -> float:
    return length * width
def area_triangle(base: float, height: float) -> float:
    return base * height * 0.5

def main():
    print("1) Circle\n2) Square\n3) Rectangle\n4) Triangle\n5) Quit\n")
    num = int(input("Which shape?(Input a number) "))

    if num == 1:
        radius = float(input("Radius: "))
        print(f"The area is {area_circle(radius)}")
    elif num == 2:
        side = float(input("Side: "))
        print(f"The area is {area_square(side)}")
    elif num == 3:
        length = float(input("Length: "))
        width = float(input("Width: "))
        print(f"The area is {area_rectangle(length, width)}")
    elif num == 4:
        base = float(input("Base: "))
        height = float(input("Height: "))
        print(f"The area is {area_triangle(base, height)}")
    elif num == 5:
        print("Goodbye.")
        quit

if __name__ == "__main__":
    main()
