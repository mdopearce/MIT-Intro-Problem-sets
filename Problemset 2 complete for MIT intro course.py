# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:59:20 2019

Problem 1
balance - outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal.
This program should calculate the remaining balance on an account of the 
variables as defined above, for exactly one year.
"""



def BalanceCheck(balance,annualInterestRate,monthlyPaymentRate):
    n=12
    while n>0:
        balance=(balance-balance*monthlyPaymentRate)
        balance=balance+balance*annualInterestRate/12
        n-=1
    return balance
        
    
"""
Problem 2
balance - outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
This function should determine the minimum monthly payment required to fully
pay off this credit card in 12 months.
It will be rounded to the nearest $10 unit of payment, and thus,
may end up resulting in a negative value at the end."""

def PaymentCheck(balance,annualInterestRate):
    #following line is present value annuity formula solved for payment
    payment=balance/((1-(1+annualInterestRate/12)**-12)/(annualInterestRate/12))
    #the following line is just working out the rounding
    payment=100*round(payment/100,1)
    return payment

"""
Problem 3
balance - outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
Same idea, but isntead of using the formula, using a bisection search. 
Instructions should be to enter only balance and annualInterestRate
"""  
    
    
def paymentCheckBisection(balance,annualInterestRate):
    payment=balance/12
    lowerBound=balance/12
    upperBound=balance*(1+annualInterestRate)**12/12
    if balance==payment*(1-(1+annualInterestRate/12)**-12)/(annualInterestRate/12):
        return payment
    else:
        def bsearch(balance,annualInterestRate,lowerBound,upperBound):
            payment=(lowerBound+upperBound)/2
            n=12
            test=balance
            while n>0:
                test=(test-payment)*(1+annualInterestRate/12)
                n-=1
            if -0.05<test<0.05:
                return round(payment,2)
            elif test>0.05:
                return round(bsearch(balance,annualInterestRate,payment,upperBound),2)
            else:
                return round(bsearch(balance,annualInterestRate,lowerBound,payment),2)
        return round(bsearch(balance,annualInterestRate,lowerBound,upperBound),2)
        
       
        
        

