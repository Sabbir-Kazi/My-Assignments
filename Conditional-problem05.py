temp=float(input("input temperature in celsius"))

#print(temp,"°C"), for degree symbol (Alt+0176)
Fahrenheit=((temp*1.8)+32)
Kelvin=(temp+273.15)

if (temp>0):
    print(Fahrenheit, "°F")

else:
    print(Kelvin,"K")