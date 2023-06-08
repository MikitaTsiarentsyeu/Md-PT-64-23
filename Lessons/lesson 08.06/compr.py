l = []
for i in range(10):
    l.append(i)

print(l)

print(list(range(10)))

l = []
for i in range(10):
    l.append(str(i))

print(l)

print([str(i) for i in range(10)])
print({str(i) for i in range(10)})
print({i:str(i) for i in range(10)})

gen = (str(i) for i in range(10))
print(list(gen))


l = []
for i in range(10):
    if i%2 == 0:
        l.append(str(i))

print(l)

print([str(i) for i in range(10) if i%2 == 0 or i>4])

test_str = "abc"
print([s*i if i > 0 else test_str for s in test_str for i in range(5)])

for i in range(5):
    for s in test_str:
        s*i