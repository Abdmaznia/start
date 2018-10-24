
value_commodity= int(input("Enter Currency Value commodity: "))
n = int(input("Enter For how many Year: "))
inflation = int(input("Enter Rate inflation: "))
print("Year Price")

for i in range (1,n+1):
    p = p +(p * inc / 100)
    print(i ,"      ",p)
