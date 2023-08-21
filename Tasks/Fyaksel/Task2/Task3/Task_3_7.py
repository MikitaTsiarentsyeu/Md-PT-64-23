# Write a program that takes a string as input and returns the string with all capital letters converted to lowercase and vice versa.
import string
string1 = input("Input string values:  ")
print(string1.swapcase())
def big_small(enter):
    str_l = string.ascii_lowercase
    str_u = string.ascii_uppercase
    d_u = dict(zip(str_u, str_l))
    d_l = dict(zip(str_l, str_u))
    out_s = ''
    for i in string1:
        if i in d_u:
            out_s += d_u[i]
        elif i in d_l:
            out_s += d_l[i]
        else:
            out_s += i
    return out_s
result = big_small(string1)
print (result)

