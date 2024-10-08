# Create a while loop that will:

# calculate the sum of the numbers from 1 to 10.
count = 0
total = 0
while count <= 10:
  total += count
  count += 1
print(total)

# calculate the sum of the numbers from 100 to 200.
count = 100
total = 0
while count <= 200:
  total += count
  count += 1 
print(total)

# calculate the difference between the sum of the numbers from 100 to 200 and the sum of the numbers from 200 to 300.
count = 100
total = 0
while count <= 200:
  total += count
  count += 1 

number = 200
amount = 0
while number <= 300
  amount += number
  number += 1

print(amount - total)

# calculate the sum of the multiples of 5 between the numbers 1000 and 10000.
count = 1000
total = 0
while count <= 10000:
  total += count
  count += 5
print(total)
  
# calculate the sum of the multiples of 5 between 1 and 100, 
# but do not include numbers that are multiples of 3. Modulus (%) will come in handy here.
count = 1
total = 0

while count <= 100:
    if count % 5 == 0 and count % 3 != 0:
        total += count
    count += 1

print(total)
