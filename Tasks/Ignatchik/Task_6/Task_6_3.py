def sum_of_numbers(l):
    try:
        if isinstance(l,list) == False:
            raise TypeError("The input is not a list")
        else:
            if all(map(lambda x: True if type(x) == int else False, l)):
                return sum(list(filter(lambda x: x%2 == 0, l)))
            else:
                raise TypeError("Not every element is int")
    except TypeError as te:
        return te
    
print(sum_of_numbers([1,2,4,'hj']))
print(sum_of_numbers([1,2,4,'44']))
print(sum_of_numbers([1,2,4,44]))
print(sum_of_numbers('1234'))



