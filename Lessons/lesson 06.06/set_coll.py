s = {1,2,3}
print(s, type(s))

s = set()
print(s, type(s))

s = set("test string with some letters")
print(s)

l1 = [1,2,3,3,3,3,3,3,3,3,3,3]
l2 = [3,2,1]
print(l1 == l2)
print(set(l1) == set(l2))

s = {1, 2.0, "str", (1,2,3,4)}
print(s)

s.add(1)
print(s)
s.add(2)
print(s)
s.add(3)
print(s)


s.update("test str")
print(s)

s.remove(1)
print(s)

# s.remove(1)
# print(s)

s.discard(1)
print(s)

print(s.pop())
print(s)
print(s.pop())
print(s)

s.clear()
print(s)

print({1,2,3}.union({2,3,4}))
print({1,2,3}.intersection({2,3,4}))
print({2,3}.issubset({2,3,4}))

test_str = "some test string with duplicated symbols"
print(''.join(set(test_str)))

test_lst = [3,56,34,2,3,5,7,5,34,2,2,3,4,4,23,3]
print(list(set(test_lst)))
