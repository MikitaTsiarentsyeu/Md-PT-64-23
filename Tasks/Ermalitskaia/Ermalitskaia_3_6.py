str1 = input()
vowel = 'aeuoiAEUOI'
str2 = ''
for i in range(len(str1)):
    if str1[i] not in vowel:
        str2 = str2 +str1[i]
print(str2)