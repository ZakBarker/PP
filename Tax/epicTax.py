import taxFunctions as tf

earnings = float(input("Annual Income: "))

tax = tf.calculateTax(earnings)
netIncome = tf.calculateNetIncome(earnings, tax)
tf.printInfo(tax, netIncome)