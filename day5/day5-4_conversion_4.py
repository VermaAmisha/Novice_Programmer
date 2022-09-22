print("To convert radian into degree:")

# formula = 1Rad × 180/π = 57.296Deg

radian = float(input("Enter the value in radians: "))

# π = 3.1415 so, 180/pi = 180/3.1415
conversion = round((radian * (180 / 3.1415 )) , 3)
print("The value in Deg:",conversion)
