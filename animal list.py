animals = 0
animals_str = ""
while animals < 4:
    animal = input("Enter an animal ")
    if animal.lower().startswith("e"):
        break
    else:
       animals += 1
       animals_str += animal
animals_list = animals_str
print(animals_list)
    
    
