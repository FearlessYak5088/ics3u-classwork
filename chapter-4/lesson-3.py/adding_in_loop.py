number = int(input("I will add up all the numbers you give me.\nNumber: "))
sum = 0

while number != 0:
  sum += number
  number = int(input(f"The total so far is {sum}\nNumber: "))
if number == 0:
  print(f"The total is {sum}")
