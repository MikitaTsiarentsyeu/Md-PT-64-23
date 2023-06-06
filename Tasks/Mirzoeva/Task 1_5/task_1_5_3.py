km_per_hour=float(input("Enter kilometres per hour:\n"))

if km_per_hour >= 1:
    meters_per_second=(km_per_hour/3.6)
    print(str(meters_per_second)+" mps ")
else:
    print("Check entered information")