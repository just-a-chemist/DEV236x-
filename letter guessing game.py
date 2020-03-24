
import random
randomletter = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
def check_gess(letter,guess):
    if guess.isalpha():
        pass
    else:
        print("enter a letter")
    if letter == guess:
        print("Woo!")
    elif letter < guess:
        print("too high")
    elif letter > guess:
        print("Too low")
    guess = input("Guess again?")
    if guess.isalpha():
        pass
    else:
        print("enter a letter")
    if letter == guess:
        print("Woo!")
    elif letter < guess:
        print("too high")
    elif letter > guess:
        print("Too low")
    print(randomletter)
    return

check_gess(randomletter,input("enter a letter?"))



