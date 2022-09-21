print("To print multiples of any three numbers below 100:")

for n in range(101):
    
    if n % 2 == 0:
        print(n)

    elif n % 3 == 0:
        print(n)

    elif n % 5 == 0:
        print(n)

    else:
        print("0")

