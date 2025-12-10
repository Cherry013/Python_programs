import random


words = ["bamboo","Camel","Zepto","Cherry"]
word = random.choice(words).lower()
print(word)

placeholder = ""
for i in range(1,len(word)+1):
    placeholder+="_"
print(placeholder)

life = 6
cl = []
while life>0:
    display = ""
    guess = input("Guess the letter: ").lower()
    if guess not in word:
        life-=1
    elif guess in cl:
        life-=1
    for i in word:
        if guess == i:
            display+=guess
            cl.append(guess)
        elif i in cl:
            display+=i
        else:
            display+="_"

    print(display)
    if "_" not in display:
        life = True
        print("You win.")





