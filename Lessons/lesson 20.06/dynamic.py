def times(a:object, b:object):
    return a*b

print(times(2,3))
print(times([2],3))
print(times('2',3))
# print(times('2','3'))
# '2'*'3'

def times_for_int(a:int, b:int) -> int:
    """this function 
    will multiply 
    only int values"""
    if isinstance(a, int) and isinstance(b, int):
        return a*b
    
print(times_for_int('2','3'))

def input_data():
    coll = input("Plese enter values separated by ','")
    return coll.split(',')

def eq():
    l1 = input_data()
    l2 = input_data()
    # l1 == l2
    for i in l1:
        if i not in l2:
            return False
    for i in l2:
        if i not in l1:
            return False
    return True

print(eq([1,2,3], [1,2,3,4]))
print(eq([1,2,3], (2,3,1)))
print(eq(['1','2','3'], "123"))