import random
import math

def card():
    """
    this program gives the user a card
    :return: this returns the program
    """
    card = random.randint(1, 10)
    return card




def user_hit(total):
    """
    this program is to see if the user wants to hit
    :param answer: this is the user's answers
    :return: this returns the program
    """
    answer = input("would you like to hit?")
    new_card = card()
    if answer == "yes":
        return new_card + total
    else:
        return total


def main():
    card1 = card()
    card2 = card()
    print(" your first card was", card1)
    print("your second card was", card2)
    total = card1 + card2
    print("your total is", total)
    total = user_hit(total)
    if total > 21:
        print("your number is over 21, you lose")
    elif total == 21:
        print("your number is 21, you win")
    else:
        print(total)


main()