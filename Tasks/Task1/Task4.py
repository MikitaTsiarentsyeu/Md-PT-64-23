# converts some amount of money from USD to BYN, the amount and ratio are given.


USD = float(input("Enter USD (>!=0): "))
С = float(input("Enter Currency coefficient (>!=0):"))
BYN = (USD * С)


print('Currency coefficient = %.5f, USD = %0.2f, BYN = %0.2f' %(С, USD,BYN))



