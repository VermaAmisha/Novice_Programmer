#Program to generate dice rolling concept
import random
num = True
while num:
    input("Press any key to role the dice: ")
    n = random.randint(1,6)
    if n == 6:
        num = True
    else:
        num = False
    print(n)
