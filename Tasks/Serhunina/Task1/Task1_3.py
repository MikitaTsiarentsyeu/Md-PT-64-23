speed = input('Given speed:\n')

if not speed.isdigit():
    print('Wrong value of speed')
    exit(1)
else:
    
    speed = int(speed)
    meters = speed*1000
    seconds = 3600
    r = meters/seconds
    
    print(round(r,2), 'meters per second')