import random
from art import logo

def deal_cards():
    Cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(Cards)
    return card


def calcu_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, Opponent has BlackJack 🤡😇"
    elif user_score == 0:
        return "Win with a BlackJack 🤑🤑"
    elif user_score > 21:
        return "You went over, You Lose😭😭"
    elif computer_score > 21:
        return "Opponent went over, You Win😎🤤"
    elif user_score > computer_score:
        return "You Win 😜"
    else:
        return "You Lose 🥶"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    U_score = -1
    C_score = -1
    is_game_over = False

    for _ in range(2): 
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())


    while not is_game_over:
        U_score = calcu_score(user_cards)
        C_score = calcu_score(computer_cards)
        print(f"Your cards: {user_cards}, Your score: {U_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if U_score == 0 or C_score == 0 or U_score > 21:
            is_game_over = True
        else:
            choi = input("Type 'y' to get another card, type 'n' to pass: ")
            if choi == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while C_score != 0 and C_score < 17:
        computer_cards.append(deal_cards())
        C_score = calcu_score(computer_cards)

    print(f"Your final hand: {user_cards}, Your final score: {U_score}")
    print(f"Computer's final hand: {computer_cards}, computer final score: {C_score}")
    print(compare(U_score,C_score))



while input("Do you want to paly a game of BlackJack? Type 'y'--> play 'n'--> quit: ") == "y":
    print("\n"*20)
    play_game()