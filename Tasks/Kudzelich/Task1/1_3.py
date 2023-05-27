km_h = float(input("Enter your speed in kilometers per hour: "))
m_s = round(km_h * 1000 / 3600, 2)
print(f"{km_h} kilometers per hour is {m_s} meters per second")