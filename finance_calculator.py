import math
#user to choose type of investment i.e. investment or bond
print("Choose either 'investment' or 'bond' from the menu below to proceed \n\n investment - to calculate the amount of interest you'll earn on interest \n bond -  to calculate amount you'll have to pay on a home loan \n")
#take user input
input_investment_type = str(input("What is your choice? ")).upper()
#options of BOND or INVESTMENT to compare against user input
bond_input = "BOND"
investment_input = "INVESTMENT"

#if choice is incorrect
if ((input_investment_type != bond_input) and (input_investment_type != investment_input)):
    print("Incorrect selection please choose investment or bond")
#if choice is investment
elif (input_investment_type == investment_input):
    '''
    ‘P’ deposit amount
    ‘r’ is the interest entered above divided by 100, e.g. if 8% is entered, then r is 0.08.
    ‘P’ is the amount that the user deposits.
    ‘t’ is the number of years that the money is being invested for.
    ‘A’ is the total amount once the interest has been applied.

    '''
    P = float(input("How much would you like to deposit? R"))
    r = float(input("What intrest rate would you like in %? "))
    r = r/100
    t = float(input("how many years do you plan on investing? "))
    interest = input("Would you like simple or compound interest [simple/compound]? ").upper()
    #if simple interest
    if (interest == "SIMPLE"):
        A = P * (1 + r*t)
        #user answer
        print("Your total amount for simple interest is R{:.2f}".format(A))
    #if compound interest
    elif (interest == "COMPOUND"):
        A = P * math.pow((1+r),t)
        #user answer
        print("Your total amount for compound interest is R{:.2f}".format(A))
#if bond is selected
elif (input_investment_type == bond_input):
    '''
    ‘P’ is the present value of the house.
    ‘i’ is the monthly interest rate, calculated by dividing the annual
    interest rate by 12.
    ‘n’ is the number of months over which the bond will be repaid.
    ‘x’ is the amount monthly to be paid
    '''
    P = float(input("What is the present value of the house? R"))
    r = float(input("What intrest rate would you like in %? "))
    r = r/(100*12)
    t = float(input("how many months do you plan on investing? "))
    x = P*((r*((r+1)**t))/(((r+1)**t)-1))
    #user answer
    print("The monthly repayment will be R{:.2f}".format(x))
