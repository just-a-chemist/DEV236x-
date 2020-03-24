def favcol(fc):
    if fc == "r".upper():
        print("Red")
    elif fc == "o".upper():
        print("Orange")
    elif fc == "y".upper():
        print("Yellow")
    elif fc == "g".upper():
        print("Green")
    elif fc == "b".upper():
        print("Blue")
    elif fc == "o".upper():
        print("Indigo")
    elif fc == "V".upper():
        print("Violet")
    else:
        print("Enter a rainbow colour!")
    return

favcol((input("Enter a rainbow colour?")).upper())
