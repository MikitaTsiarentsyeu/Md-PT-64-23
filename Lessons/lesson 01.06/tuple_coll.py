t = (1,2,3)
print(t, type(t))

t = (1,"test",[1,2,3])
print(t)

t = ()
print(t, type(t))

t = (1,)
print(t, type(t))

t = 1,
print(t, type(t))

t = tuple([1])
print(t, type(t))

t = (1,"test",[1,2,3])

# t[0] = "new first elem" error
print((1,2,3)+(4,5,6))
print(t[2][0])
t[2][0] = "new first elem"
print(t[2][0])
print(t)

l = [1,2,3,4]

t = (l,5,6,7,8,9,10)
print(t)
l[0] = 1.0
print(t)

print(len(t))
