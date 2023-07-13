a = [int(x) for x in input().split(' ')]
c = set(a)
c = list(c)
c.remove(max(c))
print(max(c))