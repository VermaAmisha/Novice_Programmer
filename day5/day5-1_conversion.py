print("To convert degree Celcius to degree Farenheit:")

# formula = (0°C × 9/5) + 32 = 32°F
# 0°C = 32°F

degree = float(input("Enter the temperature in °C: "))
conversion = (degree * 9/5) + 32

print("Temperature in °F:" , conversion)

print("To convert degree Fahrenheit into degree celcius:")

degree = float(input("Enter the temperature in °F: "))

# formula = (32°F − 32) × 5/9 = 0°C
conversion = round(((degree - 32) * 5/9) , 3)

print(conversion)
