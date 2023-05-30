
x = "test"
y = 'test'

print(x == y)

x = '''some text'''

y = """some text"""

#some comment

print(x == y)

x = """line 1
line 2
line 3"""

print(x)

print(str(print))
print(repr(print))

print(bool(''))
print(bool(' '))

my_str = "my very long string"
print(my_str, repr(my_str))
print(len(my_str))
print(my_str[0], my_str[1], my_str[2])
print(my_str[-1], my_str[-2], my_str[-3])
print(repr(my_str[2]))

print(my_str[len(my_str)-1])

print(my_str[0:7])
print(my_str[3:])
print(my_str[3:-3])
print(my_str[3:-3:3])
print(my_str[::-1])

print('s' in my_str)
print('str' in my_str)
print('test' in my_str)

print(my_str.find('y'))
print(my_str.find('very'))
print(my_str.find('test'))