# Temprature conversion using functions 
temp = int(input("\nEnter the temperature:"))
unit = input("\nEnter the unit:")
def cel(temp,unit):
    far = (temp *1.8)+ 32
    print(f"{temp}°C converted to {far}°F")
def farn(temp,unit):
    cels = (temp - 32) / 1.8
    print(cels)
if unit == "C":
    cel(temp,unit)
elif unit == "F":
    farn(temp,unit)