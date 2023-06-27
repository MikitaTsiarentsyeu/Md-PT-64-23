def summa_1(a,b):
    return a + b
print(summa_1(3,4))



def summa_2(x,y,operation):
    s = str(x)+ operation + str(y)
    return eval(s)
print(summa_2(3,4, '+'))