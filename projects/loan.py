print("Rate the folowing conditions 1-10:")
loan_size= int(input("How large is the loan?"))
credit_his= int(input("How good is your credit history?"))
income= int(input("How high is your income?"))
down_payment= int(input("How large is your down payment?"))
print(" ")
should_loan= False
if loan_size >= 5:
    if credit_his >= 7 and income >= 7:
        should_loan= True
    elif credit_his >= 7 or income >= 7:
        if down_payment >= 5:
            should_loan= True
        else:
            should_loan= False
    else:
        should_loan= False
else:
    if credit_his < 4:
        should_loan=False
    else:
        if income >=7 or down_payment >= 7:
            should_loan= True
        elif income >=4 and down_payment >= 4:
            should_loan= True
        else:
            should_loan= False
if should_loan:
    print("The decision is yes. This is a good loan.")
else:
    print("The decision is no. You should not loan this money.")
