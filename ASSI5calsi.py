
x = float(input("Enter a first number: "))
y = float(input("Enter a Second number: "))
o = input("Enter a operator(+ - * / %): ")
if o =='+':
    print("Addition is: ",x+y)
elif o =='-':
    print("substraction is: ",x-y)
elif o =='*':
    print("multiplication is: ",x*y)
elif o =='/':
    if y ==0:
        print("Enter a valid number")
    else:
        print("division is: ",x/y)
else:
    print("Enter a valid number")