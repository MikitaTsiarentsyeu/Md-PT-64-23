stroka = input('Please enter the string: ')
new_stroka = ''
for i in stroka:
    if i.islower() == True:
        new_stroka += i.upper()
    else:
        new_stroka += i.lower()
print(new_stroka)
