
usd=float(input("Enter USD:\n"))
rates=float(input("Enter rate:\n"))
byn = (usd * rates)
if usd > 0 and rates > 0:
    print("BYN =",round(byn, 1))
else:
    print("Wrong data.")


