def str_analysis(usr_input):
    while usr_input == "":
        print("Enter some text!")
        usr_input = input("Enter an integer or word. ")
    if usr_input == " ":
        print("FFS a space!")
        return "hello"
    elif usr_input.isdigit():
        if int(usr_input) > 99:
            print("Big number!")
        else: print("That;s small")
    elif usr_input.isalpha():
        print("That;s a nice word")
    else: print("That is not an integer or word.")
        
        
    
str_analysis(input("Enter an interger or word. "))
