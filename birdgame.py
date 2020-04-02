def bird():
    type = "chicken, duck, turkey"
    guess1 = input("First attempt, guess a bird ")
    if guess1.lower() not in type:
        print("You are incorrect!")
        guess2 = input("Second try. ")
        if guess2.lower() not in type:
            print("You are wrong again. Final try")
            guess3 = input("FINAL GUESS ")
            if guess3.lower() not in type:
                print("Not this time")
            else: print("Finally")
        else: print("correct")
    else: print("first try")
    
bird()
    
        
