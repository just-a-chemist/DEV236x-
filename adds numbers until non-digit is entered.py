number = input("Enter a number ")
while number.isdigit():
    number1 = int(number)
    sum = 0
    sum += number1
    number = input("Enter a number ")
    if number.isdigit() is False:
        break
    number1 = int(number)
if number.isdigit() is False:
    print("Please enter a number")    
print(sum)
