speed = input('Given speed:\n')
speed = int(speed)

meters = speed*1000

seconds = 3600

r = meters/seconds

print(round(r,2), 'meters per second')