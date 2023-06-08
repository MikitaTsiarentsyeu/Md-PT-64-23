l = [1,2,3,4,5]

swap = l[1]
l[1] = l[2]
l[2] = swap

print(l)

l[1], l[2] = l[2], l[1]
print(l)