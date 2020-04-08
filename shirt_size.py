# initial quantities
small = 0
medium = 0
large = 0
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
        print("Quitting\nSmall = ",small,"\nMedium =")
        break
    else: print("Please enter a valid shirt size or close the program.")
