def str_analysis(string):
    if string.isdigit():
        number = int(string)
        if number > 99:
            print("big number!")
        else: print("small number")
    elif string.isalpha():
        word = string.title()
        print(word,"is a nice word.")
    else: print("Is not a number or one word.")
        
        
str_analysis(input("Type a string. "))        
