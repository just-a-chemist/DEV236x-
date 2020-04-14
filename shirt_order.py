available_c = False
available_s = False
print("Welcome to Matt's Shirts. We have white shirts available in medium and large, and our blue shorts are availibe in sizes medium and large.")
shirt_colours = ("Blue, white")
shirt_blue = ("M, S")
shirt_white = ("L, M")
while available_c == False:
    shirt_colour = input("What colour of shirt would you like? ")
    if shirt_colour.lower() in shirt_colours.lower():
        available_c = True
        if available_c == True:
            shirt_size = input("What size of shirt would you like? Type S for small, M for medium, and L for Large. ")
            while shirt_colour.lower() == "blue":
                if shirt_size.lower() in shirt_blue.lower():
                    available_s = True
                    print("Shirt colour and size available.")
                    break
                else: print("Shirt size in this colour not available.")
                shirt_size = input("What size of shirt would you like? Type S for small, M for medium, and L for Large. ")
            while shirt_colour.lower() == "white".lower():
                if shirt_size.lower() in shirt_white.lower():
                    available_s = True
                    print("Shirt colour and size available.")
                    break
                else: print("Shirt size in this colour not available.")
                shirt_size = input("What size of shirt would you like? Type S for small, M for medium, and L for Large. ")
        proceed = input("Proceed to order? Y to continue, N to cancel ")
        if proceed.lower() == "y":
                quantity = input("How many would you like to order? ")
        else: print("order cancelled")
if available_c and available_s == True:
    print("Order confirmed. You have ordered",quantity,"shirts")
