string = input('Please enter the string: ')
for i in string:
    if i in 'aeyuioуеыаоэяиюОУЕЫАОЭЯAEYUIO':
        string = string.replace(i, '')
print(string)
