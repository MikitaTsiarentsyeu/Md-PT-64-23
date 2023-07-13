def calc_symb(str1,symb1):
    if len(str1) == 0:
        return 0
    if str1[0] == symb1:
        return 1 + calc_symb(str1[1:],symb1)
    else:
        return 0 + calc_symb(str1[1:],symb1)

print(calc_symb('abababab','a'))