monthly_interest_rate = annualInterestRate / 12

for i in range(1, 13):
    interest = (balance - monthlyPaymentRate *  balance)  * monthly_interest_rate
    min_payment = monthlyPaymentRate *  balance
    balance = balance - (monthlyPaymentRate *  balance) + interest

print ("Remaining balance: ", round(balance,2))
