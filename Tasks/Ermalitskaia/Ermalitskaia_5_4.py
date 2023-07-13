def count_letters(*args):
    count_capital = 0
    count_small = 0
    args1 = str(args)
    for j in args1:
        if j.isupper() == True:
            count_capital = count_capital + 1
        if j.islower() == True:
            count_small = count_small + 1
    print(count_capital)
    print(count_small)

count_letters('sdfg1456KL')

