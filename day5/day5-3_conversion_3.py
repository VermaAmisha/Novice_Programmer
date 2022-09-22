print("To convert Kelvin into degree Celcius:")

# formula = 0K − 273.15 = -273.1°C
# 0K = -273.15°C
degree = float(input("Enter the temperature in K: "))
# round off upto 3 decimal places
conversion = round((degree - 273.15), 3)
print("Temperature in °C:" , conversion)

print("To convert degree Celcius into Kelvin:")

# formula = °C + 273.15 = 273.15K
# °C = 273.15K

degree = float(input("Enter temperature in °C: "))
conversion = round((degree + 273.15) , 3)

print(conversion)
