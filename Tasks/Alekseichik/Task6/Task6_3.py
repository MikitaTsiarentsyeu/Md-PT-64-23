inp_1 = [1,2,3,4,5,6,7,8,9,10]
inp_2 = 1,2,3,4,5,6,7,8,9,10
inp_3 = ['one',2,inp_1]


def even_sum(inp):
    try:
        if not isinstance(inp,list):
            raise TypeError
        res =[]
        for i in inp:
            if i%2 == 0:
                res.append(i)
        return(sum(res))
    except TypeError:
        return('Invalid input.')

print(even_sum(inp_2))