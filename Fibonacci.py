# Fibonacci Number
# https://goo.gl/AkRPSc persian
#https://goo.gl/FWiVWM  English

f1 = 1
f2 = 1
n = int(input("Enter a Fibonacci Number:> "))
if n == 1:      # # if user input 2 print(f1  and f2)
    print(f1)
    exit(0)     # quitter
elif n == 2:    # if user input 2 print(f1  and f2)
    print(f1)
    print(f2)
else:           #  start Fibonacci number here
    print(f1)
    print(f2)
    i = 3        # count
    while i <= n:   
        f3 = f1+f2
        print(f3," ")
        f1 = f2
        f2 = f3
        i = i + 1 

