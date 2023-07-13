a = [int(x) for x in input().split(' ')]
b = []
for i in a:
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
    if flag == 0:
        b.append(i)
print(max(b))