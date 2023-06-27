def str_rev(*args):
    new_list = []
    args1 = list(args)
    for i in range(len(args1)):
        args2 = args1[i]
        args3 = args2[::-1]
        new_list.append(args3)
    print(new_list)
str_rev('mama', 'papa', 'dada')
