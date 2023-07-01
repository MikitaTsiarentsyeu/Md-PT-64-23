def reversed(list, res=[]):
    for i in list:
        i = i[::-1]
        res.append(i)
    print(f"the list with reversed strings:", res)

list = input("enter strings separated by space:\n").split()

reversed(list)