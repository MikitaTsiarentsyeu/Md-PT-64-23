def length_greater_5(list, res=[]):
    for i in list:
        if len(i)>5:
            res.append(i)
    print(res)

list = input("enter strings separated by space:\n").split()
length_greater_5(list)