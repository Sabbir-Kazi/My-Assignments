H=float(input("your height in meter= "))
W=float(input("your weight in kg= "))
BMI=W/(H**2)

print(BMI)

if (BMI<18.5):
    print("under weight")

elif (BMI>=18.5) and (BMI<=24.9):
    print("normal")

elif (BMI>=25) and (BMI<=29.9):
    print("overweight")

# elif (BMI>=30):
    print("obese")

else:
    print("you are in danger")