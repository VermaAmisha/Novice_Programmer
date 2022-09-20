print("To find simple interest of a sum:")

p = float(input("Enter principal money in Rs.: "))
r = float(input("Enter rate of interest in %: "))
t = float(input("Enter time in years: "))

simple_interest = (p * r * t)/100
amount = p + simple_interest

print("SI: Rs.", simple_interest)
print( "Amount: Rs." , amount)
