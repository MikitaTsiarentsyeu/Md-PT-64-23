l = [1,2,3]
print(l, type(l))

l = []
print(type(l), l, len(l))

l = [1,2,3,4,5,6.0,7.0,"test"]
print(l)

print([1,2,3]+[4,5,6])
print(l[0], l[1], l[-1])
print(l[1:4])

print('3' in l)

print(list("test"))

l[0] = 1.0
print(l)

l.append("new elem")
print(l)

l.extend("new elem")
print(l)

l.insert(0, "new first elem")
print(l)

l.remove(2)
print(l)

print(l.pop())
print(l)

print(l.pop(0))
print(l)

del l[0]
print(l)

del l[2:6]
print(l)

# del l
# print(l)

l.clear()
print(l)

l1 = [1,2,3]
l2 = [1,2,3]
print(l1 == l2)

l = [[[[[[[0]]]]]]]
print(l[0][0][0][0][0][0][0])

l = [[1,2,3], [4,5,6], [7,8,9]]
l[1][1]
print(l[0][0], l[0][1], l[0][2])
print(l[1][0], l[1][1], l[1][2])
print(l[2][0], l[2][1], l[2][2])

l = []
l.append(l)
print(l)
print(l[0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0])

