# without using "math" module
print("To find the remainder of two numbers:")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

remain = num1 % num2
print(remain)

# with using "math" module
 
from math import remainder

print("To find the remainder of two numbers:")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

remain = remainder(num1 , num2)

print(remain)
