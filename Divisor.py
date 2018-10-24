while True:
    num = int(input("Enter a number:>"))
    sum = 0
    for i in range(1,num):
        if (num % 1 == 0):
            sum +=i
    if (sum == num):
        print("\t","Perfacted")
    else:
        print("\t","Not Perfacted")
    yes = input("continue:> ")
    if (yes[0] == "N" or yes[0]=='n'):
        break