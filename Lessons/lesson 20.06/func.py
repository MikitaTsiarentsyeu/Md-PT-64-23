# test_sum(2, 3) error

def test_sum(a, b):
    res = a+b
    print(res)
    # return res

print(test_sum(1,2))


def level_2():
    print("level 2")

def level_1():
    print("level 1")
    level_2()


level_1()

# def func(): pass

# new_func_var = func

# print(id(func), id(new_func_var))

# sign = ""
# if sign == "+":
#     def func(a, b):
#         return a+b
# if sign == "*":
#     def func(a, b):
#         return a*b
    
def func(a, b, sign):
    if sign == "+":
        return a+b
    if sign == "*":
        return a*b

print(func(2, 3, "*"))



def print_numbers(a, b, c):
    print(id(a), id(b), id(c))
    print(a, b, c)
    a[0] += 2
    b[0] += 2
    c[0] += 2
    print(id(a), id(b), id(c))
    print(a, b, c)

var_1 = [1]
var_2 = [2]
var_3 = [3]
print(id(var_1), id(var_2), id(var_3))
print_numbers(var_1,var_2,var_3)
print(id(var_1), id(var_2), id(var_3))
print(var_1, var_2, var_3)
# print_numbers(3,2,1)
# print_numbers(3,2,input())


def test_func():
    print("before return")
    return
    return 1,2,3,4,5,"test"
    print("after return")

print(test_func())

def func_without_return():
    pass

print(func_without_return())