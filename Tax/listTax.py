earnings = float(input("Yearly Earnings: "))
tax = 0
afterTax = 0
brackets = [18200, 37000, 90000, 180000]
penalty = [3572, 20797, 54097]
rate = [0.19, 0.325, 0.37, 0.45]

if earnings <= brackets[0]:
    print("Tax Payable", earnings, "\nNet Income:", earnings)
elif earnings <= brackets[1]:
    tax = (earnings - brackets[0]) * rate[0]
    afterTax = earnings - tax
    print("Tax Payable:", tax, "\nNet Income:", afterTax)
elif earnings <= brackets[2]:
    tax = (earnings - brackets[1]) * rate[1]
    tax += penalty[0]
    afterTax = earnings - tax
    print("Tax Payable:", tax, "\nNet Income:", afterTax)
elif earnings <= brackets[3]:
    tax = (earnings - brackets[2]) * rate[2]
    tax += penalty[1]
    afterTax = earnings - tax
    print("Tax Payable:", tax, "\nNet Income:", afterTax)
else:
    tax = (earnings - brackets[3]) * rate[3]
    tax += penalty[2]
    afterTax = earnings - tax
    print("Tax Payable:", tax, "\nNet Income:", afterTax)