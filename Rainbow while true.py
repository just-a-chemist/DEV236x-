# [ ] use a while True loop (forever loop) to give 4 chances for input of a correct color in a rainbow
# rainbow = "red orange yellow green blue indigo violet"
guess = 0
rainbow_colours =("red","orange","yellow","green","blue","indigo","violet")
while guess < 4:
    usr = input("Enter a colour in the rainbow. ")
    if usr.lower() in rainbow_colours:
        print("Correct!")
        break
    else: guess += 1

if guess >= 4: print("Wrong!")
    
