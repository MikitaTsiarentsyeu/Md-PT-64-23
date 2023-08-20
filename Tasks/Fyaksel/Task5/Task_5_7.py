def palind(str1):
    if len(str1) == 0:
        return str1
    else:
        a1 = str1[0]
        a2 = str1[1:-1]
        a3 = str1[-1]
        return a1 == a3 and palind(a2)
str2 = [i.lower() for i in input() if i.isalpha()]
palind(str2)
print(str2)