stroka = input('Please, enter the string: ').lower()
vowels = 0
for i in stroka:
    if i in 'aeyuioуеыаоэяию':
        vowels += 1
print(vowels)
