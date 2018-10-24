while True:
    much = int(input("How Much money Do you need: "))
    installments = int (input("Enter the number of installments: ")) 
    interest_rate = int (input("Enter interest rate:"))
    Totalـpaidـloan = (12  * much) / (12 - installments * interest_rate / 100)
    payment = Totalـpaidـloan / installments
    print("Total_paid_loan:",Totalـpaidـloan,'\t',payment)
    Continuation = input("Do you want to countinue (y/n):")
    if Continuation [0] == "n":
        break
        