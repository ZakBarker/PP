import taxFunctions as tf

for i in range(1, 11):
    earnings = i * 16592
    tax = tf.calculateTax(earnings)
    netIncome = tf.calculateNetIncome(earnings, tax)
    print("Earnings:", earnings)
    tf.printInfo(tax, netIncome)
    print('')
