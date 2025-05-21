operator=input("operator(+, -, *, /):")
num1=float(input("enter 1st number"))
num2=float(input("enter 2nd number"))

if operator=="+":
    print(num1+num2)

elif operator=="-":
    print(num1-num2)

elif operator=="*":
    print(num1*num2)

elif operator=="/":
    print(num1/num2)

else:
    print("calculation is invalid")