x = 'asdBNMavMN'

def count(x):
    up = 0
    low = 0
    for i in x:
        if i.isupper():
            up += 1
        else:
            low += 1

    return up, low

print(count(x))