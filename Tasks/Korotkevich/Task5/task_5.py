x = [0,1,2,4,5,6,7,10]

def list_coll(x):
    res = ''
    x.append(0)
    first = 0
    last = 0
    single = 0
    for i in range(len(x)-1):
        if x[i]+1 == x[i+1]:
            if first == 0:
                first = x[i]
        elif x[i]+1 != x[i+1] and x[i]-1 == x[i-1]:
            last = x[i]
        elif x[i]-1 != x[i-1] and x[i]+1 != x[i+1]:
            if single == 0:
                single = x[i]
        if last != 0:
            res +=(f'{str(first)}-{str(last)}, ')
            first = 0
            last = 0
        elif single != 0:
            res +=f'{str(single)}, '
            single = 0
    print(res[:-2])


list_coll(x)