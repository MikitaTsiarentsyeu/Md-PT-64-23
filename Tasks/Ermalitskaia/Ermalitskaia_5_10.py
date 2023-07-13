def fib1(n):
    list1 = []
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    list1 = [1, 1]
    for i in range (2, n):
        list1.append(list1[-1] + list1[-2])
    return list1
n1 = int(input())
print(fib1(n1))
