def reverse_str(str1):
    if len(str1) == 0:
        return str1
    else:
        return reverse_str(str1[1:]) + str1[0]
str2 = input()
print(reverse_str(str2))