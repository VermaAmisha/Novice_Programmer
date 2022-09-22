print("To convert degree Fahrenheit to Kelvin:")

# formula = (32°F − 32) × 5/9 + 273.15 = 273.15K
# 32°F = 273.15 K
degree = float(input("Enter the temperature in °F: "))
# round off upto 3 decimal places
conversion = round(((degree - 32) * 5/9 + 273.15) , 3)

print("Temperature in Kelvin:" , conversion)

print("To convert Kelvin to Fahrenheit:")

degree = float(input("Enter the temterature in K: "))

# (0K − 273.15) × 9/5 + 32 = -459.7°F
conversion = (degree - 273.15) * 9/5 + 32

print("Temperature in °F:" , conversion)
