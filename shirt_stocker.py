# initial quantities
small = 0
medium = 0
large = 0
sc = 10
mc = 12
lc = 15
while True: 
    shirt_size = input('Enter a shirt size or exit to finish. ')
    
    if shirt_size.lower().startswith("s"):
        small = small + 1
        print(small)
    elif shirt_size.lower().startswith("m"):
        medium += 1
    elif shirt_size.lower().startswith("l"):
        large += 1
    elif shirt_size.lower().startswith('e'):
        print("Quitting.....\n......\nSmall = ",small,"\nMedium =",medium,"\nLarge =",large,"\nThe total value of small shirts is $"+str(sc * small)+"\nThe total value of medium shirts is $"+str(mc * medium)+"\nThe total value of large shirts is $"+str(lc * large))
        break
    else: print("Please enter a valid shirt size or close the program.")
