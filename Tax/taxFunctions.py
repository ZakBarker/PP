def calculateTax(earnings):
    brackets = [18200, 37000, 90000, 180000]
    penalty = [3572, 20797, 54097]
    rate = [0.19, 0.325, 0.37, 0.45]

    if earnings <= brackets[0]:
        tax = 0
    elif earnings <= brackets[1]:
        tax = (earnings - brackets[0]) * rate[0]
    elif earnings <= brackets[2]:
        tax = ((earnings - brackets[1]) * rate[1]) + penalty[0]
    elif earnings <= brackets[3]:
        tax = ((earnings - brackets[2]) * rate[2]) + penalty[1]
    else:
        tax = (earnings - brackets[3]) * rate[3] + penalty[2]

    return (tax)


def calculateNetIncome(earnings, tax):
    return earnings - tax


def printInfo(tax, netIncome):
    print("Tax Payable:", tax, "\nNet Income:", netIncome)