import re

time = input('Enter time (hh:mm):\n')

if not re.match(r'^[0-2][0-9]:[0-5][0-9]$', time):
    input('Error. Input format must be like hh:mm and only digital.\n Press Enter to exit.')
    exit()
else:
    hh, mm = time.split(':')

val_0_2 = {0:'ноль', 1:'час',2:'два'}
val_0_12 = {1:'первого', 2:'второго', 3:'третьего', 4:'четвертого', 5:'пятого', 6:'шестого', 7:'семого', 8:'восьмого', 9:'девятого', 10:'десятого', 11:'одинадцатого',12:'двенадцатого',13:'первого'}
val_1_29 = {0:'ноль',1:'одна', 2:'две', 3:'три', 4:'четыре', 5:'пять', 6:'шесть', 7:'семь', 8:'восемь', 9:'девять', 10:'десять', 11:'одиннадцать',12:'двенадцать',13:'тринадцать',14:'четырнадцать',15:'пятнадцать',16:'шестнадцать',17:'семнадцать',18:'восемнадцать',19:' девятнадцать',20:'двадцать',21:'двадцать одна',22:'двадцать две',23:'двадцать три',24:'двадцать четыре', 25:'двадцать пять',26:'двадцать шесть',27:"двадцать семь",28:'двадцать восемь',29:'двадцать девять'}
val_30_40 = {3:'тридцать',4:'сорок'}

if int(hh) > 12:
    hh = int(hh) - 12
else:
    hh = int(hh)

mm_int = int(mm)
mm_first = int(mm[0])
mm_second = int(mm[1])

if mm_int == 0:
    if hh == 2:
        print(f'{time} - {val_0_2[hh]} часа ровно')
    elif 2 < hh <=4:
        print(f'{time} - {val_1_29[hh]} часа ровно')
    elif int(hh) == 1:
        print(f'{time} - {val_0_2[hh]} ровно')
    else:
        print(f'{time} - {val_1_29[hh]} часов ровно')
elif 0 < mm_int < 30:
    if mm_int == 1:
        min_ending = 'минута'
    elif 2 <= mm_int <= 4 or 22 <= mm_int <= 24:
        min_ending = 'минуты'
    else:
        min_ending = 'минут'
    print(f'{time} - {val_1_29[mm_int]} {min_ending} {val_0_12[hh + 1]}')

elif mm_int == 30:
    print(f'{time} - половина {val_0_12[hh+1]}')

elif 30 < mm_int < 45:
    if mm_second == 1:
        min_ending = 'минута'
    elif 2 <= mm_second <= 4:
        min_ending = 'минуты'
    else:
        min_ending = 'минуты'
    print(f'{time} - {val_30_40[mm_first]} {val_1_29[mm_second]} {min_ending} {val_0_12[hh+1]}')
elif mm_int >= 45:
    if hh == 0 or hh == 1:
        if mm_int == 59:
            print(f'{time} - без минуты {val_0_2[hh+1]}')
        elif mm_int == 52:
            print((f'{time} - без {val_1_29[60-mm_int][:-3]}ьми минут {val_0_2[hh+1]}'))
        elif 56 <= mm_int <=57:
            print((f'{time} - без {val_1_29[60 - mm_int][:-1]}ёх минут {val_0_2[hh + 1]}'))
        elif mm_int == 58:
            print((f'{time} - без {val_1_29[60 - mm_int][:-1]}ух минут {val_0_2[hh + 1]}'))
        else:
            print((f'{time} - без {val_1_29[60 - mm_int][:-1]}и минут {val_0_2[hh + 1]}'))
    elif hh == 12:
        if mm_int == 59:
            print(f'{time} - без минуты {val_0_2[1]}')
        elif mm_int == 52:
            print((f'{time} - без {val_1_29[60-mm_int][:-3]}ьми минут {val_0_2[1]}'))
        elif 56 <= mm_int <=57:
            print((f'{time} - без {val_1_29[60 - mm_int][:-1]}ёх минут {val_0_2[1]}'))
        elif mm_int == 58:
            print((f'{time} - без {val_1_29[60 - mm_int][:-1]}ух минут {val_0_2[1]}'))
        else:
            print((f'{time} - без {val_1_29[60 - mm_int][:-1]}и минут {val_0_2[1]}'))
    else:
        if mm_int == 59:
            print(f'{time} - без минуты {val_1_29[hh+1]}')
        elif mm_int == 52:
            print((f'{time} - без {val_1_29[60-mm_int][:-3]}ьми минут {val_1_29[hh+1]}'))
        elif 56 <= mm_int <=57:
            print((f'{time} - без {val_1_29[60 - mm_int][:-1]}ёх минут {val_1_29[hh + 1]}'))
        elif mm_int == 58:
            print((f'{time} - без {val_1_29[60 - mm_int][:-1]}ух минут {val_1_29[hh + 1]}'))
        else:
            print((f'{time} - без {val_1_29[60 - mm_int][:-1]}и минут {val_1_29[hh + 1]}'))