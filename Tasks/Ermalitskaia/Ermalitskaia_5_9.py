def power1(n, m):
    if m == 0:
        return 1
    elif m == 1:
        return n
    elif m % 2 == 0:
        res = power1(n, m //2)
        return res * res
    else:
        res = power1(n, (m - 1) // 2)
        return n * res * res
n1, m1 = int(input()), int(input())
print(power1(n1, m1))