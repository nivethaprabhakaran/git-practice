#simple calculator 
while(True):
    n1=int(input("Enter first number"))
    n2=int(input("Enter second number"))
    o=input("Enter the operators\nAddition = +\nSubtraction = -\nDivision = /\nMultiplication = *\ne for exit")
    if o=="+":
        r=n1+n2
        print(f"Addition of {n1} and {n2} is {r}")
    elif o=="-":
        r=n1-n2
        print(f"Subtraction of {n1} and {n2} is {r}")
    elif o=="*":
        r=n1*n2
        print(f"Multiplication of {n1} and {n2} is {r}")
    elif o=="/":
        try:
            r=n1/n2
            print(f"Division of {n1} and {n2} is {r}")
        except ZeroDivisionError as e:
            print(e)
    elif o=="e":
        print("exiting calculator..")
        break
    else:
        print("Invalid operation")
    


#new feature to be added in future