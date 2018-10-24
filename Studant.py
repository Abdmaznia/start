id1 = -1
max1 = -1
max2 = -1
id2 = -1
n = int(input("Enter n :"))
if n < 2:
    print("Please Enter a number Greater then 1:> ") 
else:
    for i in range (1, n+1): # 
        id = int (input("Enter id:>"))
        aver = float (input("Enter Averge:>"))
        if aver > max1:
            id2 = id1
            max2 = max1
            max1 = aver
            id1 = id
        else:
            if aver >max2 :
                max2  = aver
                id2 = id
    print("max2= ",max2,"\t","id2= ",id2)
    