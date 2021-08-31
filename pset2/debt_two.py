'''
Write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

    - balance - the outstanding balance on the credit card

    - annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year.

Assume that the interest is compounded monthly according to the balance at the end of the month

The monthly payment must be a multiple of $10 and is the same for all months
it is possible for the balance to become negative using this payment scheme, which is okay.
'''

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
