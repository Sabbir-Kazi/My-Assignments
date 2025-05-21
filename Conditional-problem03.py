#Age Classifier
Age=int(input("Enter any Age"))

if (Age>=0) and (Age<=1):
    print("Infant")

elif (Age>=2) and (Age<=3):
    print("Toddler")

elif (Age>=4) and (Age<=12):
    print("Child")

elif (Age>=13) and (Age<=19):
    print("Teenager")

else:
    print("Adult")