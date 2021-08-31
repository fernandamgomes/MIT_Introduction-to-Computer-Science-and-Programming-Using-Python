monthly_interest_rate = annualInterestRate / 12
monthlyPayment = 10
unpaid_balance = balance

while True:
    for i in range(1, 13):
        interest = (unpaid_balance - monthlyPayment)  * monthly_interest_rate
        unpaid_balance = unpaid_balance - monthlyPayment  + interest
    if unpaid_balance <= 0:
        print("Lowest Payment: %d" % monthlyPayment)
        break
    else:
        monthlyPayment = monthlyPayment + 10
        unpaid_balance = balance
