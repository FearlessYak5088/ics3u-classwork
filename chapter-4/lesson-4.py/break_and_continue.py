# Create a loop that counts from 0 to 10, but skip the number 7.
num = 0
while num < 10:
  num += 1
  if num != 7:
    print(num)
  elif num == 7:
    continue

# Create a loop that will add the numbers from 5 to 20 but not any multiples of 3. Use modulus.
num = 5

while num <= 20:
    num += 1
    if num % 3 != 0:
       print(num)
    elif num % 3 == 0:
        continue

# Ask the user for a starting number and an ending number. 
# The program will get the sum of all the numbers from the start to the end (using a loop). 
# However, our program is a bit of a diva: the program will stop summing the numbers if it encounters a 13 or a 31. 
# It will still output the sum up to that point.
starting_num = int(input("Give me a starting number.\n"))
ending_num = int(input("Give me an ending number.\n"))
sum = starting_num

while starting_num <= ending_num:
  starting_num += 1
  sum += starting_num
  print(sum)
  if starting_num == 12 or starting_num == 30:
    break
    
# Create an infinite loop using while True:. In that loop ask the user for a word. 
# For each word they enter, output the following "Your word: {word}". 
# If ever they enter the word "stop" the program will break out of the loop. Finally the program will output "Goodbye!".
while True:
    word = input("Your word: ").upper()
    if word == "stop".upper():
      print("Goodbye!")
      break
      
