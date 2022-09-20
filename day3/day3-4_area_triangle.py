from math import sqrt

print("To find the area of a triangle:")

side1 = float(input("Enter length of first side in cm: "))
side2 = float(input("Enter length of second side in cm: "))
side3 = float(input("Enter length of third side in cm: "))

# area by Heron's formula
# half of perimeter "s"
s = (side1 + side2 + side3)/2
area = sqrt(s*((s-side1)*(s-side2)*(s-side3)))

print(area,"sq cm")
