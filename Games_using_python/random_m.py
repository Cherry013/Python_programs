import random

print(random.randint(0,10))

print(random.random())
print(random.uniform(1,10))

random_HT = random.randint(0,1)
if random_HT == 0:
    print("Heads")
else:
    print("Tails")


li = ["Hello","Haiii","kai","Goku","Gohan"]

li.insert(4,"Vegeta")
print(li)
print(random.choice(li))