import random
list = []

list.append(random.randint(1,100))
list.append(random.randint(1,100))
list.append(random.randint(1,100))
list.append(random.randint(1,100))
list.append(random.randint(1,100))
list.append(random.randint(1,100))
list.append(random.randint(1,100))
list.append(random.randint(1,100))
list.append(random.randint(1,100))
list.append(random.randint(1,100))

for i in range(len(list)):
    print(f"slot {i} contains a {list[i]}")
