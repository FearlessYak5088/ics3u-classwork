# Create a program that will take a string as shown below, split and convert them to actual numbers and store them in the list. 
# For example the string: one,two,three,four
# Should end up with the list: [1, 2, 3, 4]

string = "one, two, three, four"

string_int = string.split(", ")
number_words = ["one", "two", "three", "four"]
number_list = []

for word in string_int:
    for i in range(len(number_words)):
        if word == number_words[i]:
            number_list.append(i + 1)
            break

print(number_list)  
