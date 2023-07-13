x = 27

def power(x, res=0, i=3):
    if x < i:
        return res
    x //= i
    return power(x, res+1)

print(power(x))