n = int(input("How many Employee workes: ")) 
i = 1 # Counter
while i <= n:
    Employeeـname = input("Enter a identifier: ")
    Hours = int(input("Enter a work Hours: "))
    Hourly_wages = float(input("Enter a Hourly wages: "))
    overtime = 0 # overtime
    if Hours > 40:
            overtime=(3/2.0-1)*(Hours-40)*Hourly_wages
    Income=overtime+Hourly_wages* Hours
    print("Employee:",Employeeـname,"overtime: ",overtime,"Income: ",Income)
    i = i + 1
    