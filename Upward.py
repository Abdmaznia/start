a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

if a > b:
    temp = a
    a = b
    b = temp
if a > c:
    temp = a
    a = c
    c = temp
if b > c:
    temp = b
    b = c
    c = temp
print("sorted :",a,b,c)