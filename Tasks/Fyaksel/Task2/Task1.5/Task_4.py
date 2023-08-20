# converts some amount of money from USD to BYN, the amount and ratio are given.
USD = float(input("Enter the amount of USD to transfer to BYN: "))
С = float(input("Enter Cross-rate USD/BYN:"))
BYN = (USD * С)
if USD>0 and С>0:
    print('Currency coefficient = %.5f, USD = %0.2f, BYN = %0.2f' %(С, USD,BYN))
else:
    print("The values: USD and C cannot be zero or negative.")
    exit()



