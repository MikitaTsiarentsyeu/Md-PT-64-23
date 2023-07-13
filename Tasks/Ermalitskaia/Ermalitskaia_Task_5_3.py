def str_length(*args):
    new_list = []
    args1 = list(args)
    for i in range(len(args1)):
        args2 = args1[i]
        length1 = len(args2)
        count1 = 6 - length1
        if count1 <= 0:
            new_list.append(args2)
        elif count1 == 6:
            new_list.append('______')
        elif 0 < count1 < 6:
            args2 = args2 + '_' * count1
            new_list.append(args2)
    print(new_list)
str_length('m', '', 'dadada')