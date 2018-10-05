import random

card = random.randint(1, 10)


def draw_card():
    print(random.randint(1, 10))


answer = ("yes", "no")
def user_hit(answer):
    hit = input("would you like to hit?")
    if answer == "yes":
        draw_card()




def main():
    for x in range(2):
        draw_card()
    user_hit(answer)


main()