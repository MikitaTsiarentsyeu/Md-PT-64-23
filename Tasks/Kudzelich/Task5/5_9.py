def power(x,n):
    if n == 0:
        return 1
    if n < 0:
        return power(1/x, -n)
    if n%2 == 0:
        return power(x, n//2) * power(x, n//2)
    else:
        return power(x, n-1) * x

print(f"the result is", power(x:= int(input("number:\n")), n:= int(input("power:\n"))))