from functools import reduce

def apply(l, f, i=0):
    if i == len(l):
        return
    f(l[i])
    apply(l, f, i+1)

l = [1,2,3,4,5]

apply(l, print)

def print_sq(num):
    print(num*num)

# apply(l, print_sq)

lambda num: print(num*num)

apply(l, lambda num: print(num*num))

print_sq = lambda num: print(num*num)

print_sq(100)

def sum(x, y):
    return x+y

sum = lambda x, y=0: x+y
print(sum(2, 3))

cycle = lambda l, f: [f(i) for i in l]
print(cycle(l, lambda x: str(x)))

test_str = "Abc Aac aaa bbb kkk"
print(sorted(test_str.split()))
print(sorted(test_str.split(), key=lambda x: x.lower()))
print(sorted(test_str.split(), key=str.lower))

mp = map(print, l)
print(type(mp))
# for i in mp: pass
print(list(mp))

print(list(map(lambda num: chr(num*100), l)))

print(list(filter(lambda x: x, l)))

print(list(map(lambda num: chr(num*100), filter(lambda x: x>2, l))))

print(reduce(lambda x, y: x+y, l))

print(reduce(lambda x, y: f"{x}-{y}", l))

"1-2"
"1-2-3"
"1-2-3-4"
"1-2-3-4-5"

print(reduce(lambda x, y: x if x < y else y, l))

l = ['1', '11', '12', '22', '2', '13', '30', '33']
print(sorted(filter(lambda x: int(x) % 2 == 0, l), key=int))     