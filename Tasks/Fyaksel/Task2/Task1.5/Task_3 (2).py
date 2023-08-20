# converts kilometers per hour to meters per second, given the speed in kilometers per hour
kmh = float(input("Enter the speed in kilometers per hour to convert to meters in seconds:"))
mps = (kmh * 1000/3600)
if kmh > 0:
    print('%.2f kmh = %0.2f mps' %(kmh, mps))
else:
    print("If the speed is zero, then the object is not moving. No velocity can ever be negative, since it is a scalar quantity and has no direction.")
    exit()


