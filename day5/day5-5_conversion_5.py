print("To convert degree into radian:")

# 1Deg × π/180 = 0.01745Rad

degree = float(input("Enter the value in Deg: "))

# value of π = 3.1415 
conversion = round((degree * (3.1415 / 180)) , 4)

print("The value in Rad:", conversion)
