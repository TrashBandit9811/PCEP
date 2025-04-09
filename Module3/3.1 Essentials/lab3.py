income = float(input("Enter your income: "))

if income <= 85528:
    tax=(income*.018)-556.2
else:
    tax=(income - 85528) * 0.32 + 14839.2

if tax < 0.0:
    tax = 0.0

tax = round(tax, 0)
print("The tax is " , tax , "thalers")
