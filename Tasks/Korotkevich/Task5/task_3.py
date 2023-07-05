x = ['zxcvbn', 'qwe', 'qwer', 'zxcvbnma']

def larger(x):
    res = []
    for i in x:
        if len(i) > 5:
            res.append(i)
    return res

print(larger(x))