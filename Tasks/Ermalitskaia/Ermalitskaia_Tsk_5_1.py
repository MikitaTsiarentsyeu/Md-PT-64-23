def sum(a:int,b:int):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        print('Numbers should be integers')

print(sum(3,4))