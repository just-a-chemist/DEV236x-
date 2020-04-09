int_num = input("Enter a number. Any other character will result in termintaion of the program.")
long_num = ""
while int_num.isdigit() == True:
    long_num += int_num
    int_num = input("Enter a number. Any other character will result in termintaion of the program.")

print(long_num)
    
