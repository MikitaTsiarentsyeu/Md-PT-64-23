def operate(a, b, sign="+"):
    if sign == "+":
        return a+b
    elif sign == "-":
        return a-b
    elif sign == "*":
        return a*b
    elif sign == "/":
        return a/b
    
print(operate(2, 3, "*"))
print(operate(2, 3))

print(1,2,3,sep=",",end=".\n")

def my_print(*args, sep=" ", end="\n"):
    print(*args, sep=sep, end=end)

def test_func(arg=[]):
    print(id(arg))
    arg.append(1)
    print(arg)

test_func()
test_func()
test_func()