#Write a recursive function to calculate the power of a given number.
def func(g_num, power):
    if power ==0:
        return 1
    else:
        return g_num*func(g_num, power-1)

g_num = 5
power = 2
our_func = func(g_num, power)
print(our_func)
