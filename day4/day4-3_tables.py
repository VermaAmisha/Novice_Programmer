print("To search the table of any number till 10 times:")
num = int(input("Enter the number: "))

for n in range(1 , 11):
    table = num * n
    print(num , "*" , n , "=" , table)
