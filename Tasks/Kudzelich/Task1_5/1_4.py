try:
    usd = float(input("Enter the amount of money in USD:\n"))
    ratio = float(input("Enter the ratio:\n"))
    byn = round(usd * ratio, 2)
    print(f"The {usd} USD is {byn} BYN, the ratio is {ratio}")
except ValueError:
    print("You enter a wrong data")