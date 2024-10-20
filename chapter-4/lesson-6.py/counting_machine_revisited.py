start = int(input("Count from: "))
end = int(input("Count to: ")) + 1
increment = int(input("Count by: "))

for i in range(start, end, increment):
    print(i)
