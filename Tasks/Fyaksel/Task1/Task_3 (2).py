# converts kilometers per hour to meters per second, given the speed in kilometers per hour

kmh = float(input("Enter the speed in kilometers per hour (<!=0): "))
mps = (kmh * 1000/3600)
print('%.2f kmh = %0.2f mps' %(kmh, mps))



