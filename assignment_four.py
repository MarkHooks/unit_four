import random


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
    if answer == "yes" or "y":
        return new_card + total
    else:
        return total


def dealer_hit(dealer_total):
    """
    this program is to get the new card for the dealer
    :param dealer_total: this is the dealer's total
    :return: this returns the program
    """
    new_card = card()
    return new_card + dealer_total


def main():
    card1 = card()
    card2 = card()
    print("your first card was", card1)
    print("your second card was", card2)
    total = card1 + card2
    print("your total is", total)
    total = user_hit(total)
    if total > 21:
        print("your number is over 21, you lose")
    elif total == 21:
        print("your number is 21, you win")
    else:
        print("your final total is", total)
    card3 = card()
    card4 = card()
    print("my first card was", card3)
    print("my second card was", card4)
    dealer_total = card3 + card4
    print("my total is", dealer_total)
    dealer_total = dealer_hit(dealer_total)
    if dealer_total > 21:
        print("my number is over 21, I lose")
    elif dealer_total == 21:
        print("my number is 21, I win")
    else:
        print("my final total is", dealer_total)
    if total < dealer_total < 21:
        print("my number is higher than your number I win")
    elif dealer_total < total < 21:
        print("your number is higher than my number, you win")
    elif dealer_total == total:
        print("we have the same number, its a draw")


main()
