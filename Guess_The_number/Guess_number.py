import random
from art import logo

def ans_range(num,guess):
    if num > guess:
        print("Too low")
    else:
        print("Too High")

def easy(num):
    ch = 10
    win = 0
    while ch>0:
        print(f"You have {ch} chances to guess the number")
        guess = int(input("Number: "))
        if num == guess:
            win = 1
            break
        else:
            ans_range(num,guess)
            ch-=1
    if win == 1:
        print("You'r guess is correct, You have Won The game 😎😎")
    else:
        print(f"Original Number: {num}")
        print("You'r guesses are Wrong, You have Lost The game 😭😇")



def hard(num):
    ch = 5
    win = 0
    while ch>0:
        print(f"You have {ch} chances to guess the number")
        guess = int(input("Number: "))
        if num == guess:
            win = 1
            break
        else:
            ans_range(num,guess)
            ch-=1
    if win == 1:
        print("You'r guess is correct, You have Won The game 😎😎")
    else:
        print(f"Original Number: {num}")
        print("You'r guesses are Wrong, You have Lost The game 😭😇")


is_Game_on = True
while is_Game_on:
    print("\n"*10)
    print(logo)
    k = random.randint(1,101)
    print("I am thinking a number between 1 and 100 ")
    direction = input("Choose a difficulty 'easy' or 'hard': ").lower()

    if direction == "easy":
        easy(k)
    elif direction == "hard":
        hard(k)
    else:
        print("Wrong Choice entered")
    
    play = input("do you want play game? type 'y' to play otherwise 'n': ")
    if play == 'y':
        continue
    else:
        is_Game_on = False