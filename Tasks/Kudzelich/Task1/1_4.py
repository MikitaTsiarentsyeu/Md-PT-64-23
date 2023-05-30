usd = float(input("Enter the amount of money in USD: "))
ratio = float(input("Enter the ratio: "))
byn = round(usd * ratio, 2)
print(f"The {usd} USD is {byn} BYN, the ratio is {ratio}")