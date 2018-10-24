y1 = int(input("Enter Price for first Year:> "))
y2 = int(input("Enter Price for second Year:> "))
t = (float)(y2-y1) / y1 * 100
y3 = y2 + y1 * t
print("Extera = %",t,"\t\t price for next year>:",y3)