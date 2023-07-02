num = 5
power = 3

def st(num,power):
    if power == 0:
        return 1
    else:
        return num * st(num, power-1)

print(st(num,power))
