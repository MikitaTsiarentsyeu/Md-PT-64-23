velocity = input('Enter speed in kilimeters per hour:\n')

try:
    velocity = float(velocity)
except:
    print('Wrong data entered')
    exit()
if velocity >= 0:
    print('Speed in meters per hour is', velocity / 3.6)
else:
    print('Enter positive value')
