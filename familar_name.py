def familiar_name(name):
    while True:       
        if name.isalpha():
            print("Hello",name.title(),"wassup!")
            break
        else: 
            name = input("Not a familar name.\nPlease enter a familiar name. ")
    
    
    
familiar_name(input("Enter a familiar name. "))
    

    
    
