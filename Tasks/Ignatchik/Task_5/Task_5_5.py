list_input = [0, 1, 2, 3, 4, 7, 8, 10]

def nums(lst):
    res = str(lst[0])
    for n in range(len(lst) - 1):
        if lst[n] + 1 == lst[n + 1]:
            if res[-1] != '-':
                res += '-'
        else:
            if f'{lst[n]}' not in res:
                res += f'{lst[n]}, {lst[n + 1]}'
            else:
                res += f'{lst[n + 1]}'
    return res

print(nums(list_input))