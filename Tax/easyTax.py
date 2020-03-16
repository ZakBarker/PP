earnings = float(input("Yearly Earnings: "))
tax = 0
afterTax = 0

if earnings <= 18200:
    print("Tax Payable", earnings, "\nNet Income:", earnings)
elif earnings <= 37000:
    tax = (earnings - 18200) * 0.19
    afterTax = earnings - tax
    print("Tax Payable:", tax, "\nNet Income:", afterTax)
elif earnings <= 90000:
    tax = (earnings - 37000) * 0.325
    tax += 3572
    afterTax = earnings - tax
    print("Tax Payable:", tax, "\nNet Income:", afterTax)
elif earnings <= 180000:
    tax = (earnings - 90000) * 0.37
    tax += 20797
    afterTax = earnings - tax
    print("Tax Payable:", tax, "\nNet Income:", afterTax)
else:
    tax = (earnings - 180000) * 0.45
    tax += 54097
    afterTax = earnings - tax
    print("Tax Payable:", tax, "\nNet Income:", afterTax)