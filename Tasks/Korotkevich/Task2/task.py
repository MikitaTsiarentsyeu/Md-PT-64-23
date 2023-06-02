time_num = input('Please, enter the time in the format hh:mm\n' )
#валидация введенных данных
hours = time_num.split(':')[0]
minutes = time_num.split(':')[1]
if hours.isdigit() and minutes.isdigit() and 0 <= int(hours) < 24 and 0 <= int(minutes) < 60:
    hours = int(hours)
    minutes = int(minutes)
<<<<<<< Updated upstream
    if hours > 12:
=======
    if hours >= 12:
>>>>>>> Stashed changes
        hours -= 12
else:
    print('You have entered the wrong data')
    exit()
#создание необходимых словарей
hours_dict1 = {1:'час',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять',10:'десять',11:'одиннадцать',12:'двенадцать'}
<<<<<<< Updated upstream
hours_dict2 = {1:'первого',2:'второго',3:'третьего',4:'четвертого',5:'пятого',6:'шестого',7:'седьмого',8:'восьмого',9:'девятого',10:'десятого',11:'одиннадцатого',12:'двенадцатого'}
=======
hours_dict2 = {1:'первого',2:'второго',3:'третьего',4:'четвертого',5:'пятого',6:'шестого',7:'седьмого',8:'восьмого',9:'девятого',10:'десятого',11:'одиннадцатого',12:'двенадцатого',13:'двенадцатого'}
>>>>>>> Stashed changes
minutes_dict1 = {1:'одна',2:'две',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять'}
minutes_dict2 = {2:'двадцать',3:'тридцать',4:'сорок'}
minutes_dict3 = {10:'десять',11:'одиннадцать',12:'двенадцать',13:'тринадцать',14:'четырнадцать',15:'пятнадцать',16:'шестнадцать',17:'семнадцать',18:'восемнадцать',19:'девятнадцать',20:'двадцать'}
minutes_dict4 = {1:'одной',2:'двух',3:'трех',4:'четырех',5:'пяти',6:'шести',7:'семи',8:'восьми',9:'девяти',10:'десяти',11:'одиннадцати',12:'двенадцати',13:'тринадцати',14:'четырнадцати',15:'пятнадцати'}
<<<<<<< Updated upstream
#время словами без склонения слов
if minutes == 0:
    print(f'{hours_dict1[hours]} ровно')
elif minutes == 30:
    print(f'половина {hours_dict2[hours+1]}')
elif minutes >= 45:
    print(f'без {minutes_dict4[60-minutes]} минут {hours_dict1[hours+1]}')
elif 30 < minutes < 45:
    if minutes == 40:
        print(f'{minutes_dict2[minutes//10]} минут {hours_dict2[hours+1]}')
=======
#время словами со склонениями минут и часов
if hours == 0 and minutes == 0:
    print('ровно полночь')
elif minutes == 0:
    if 1 < hours <= 4:
        print(f'{hours_dict1[hours]} часа ровно')
    elif hours == 1:
        print(f'{hours_dict1[hours]} час ровно')
    else:
        print(f'{hours_dict1[hours]} часов ровно')
elif minutes == 30:
    print(f'половина {hours_dict2[hours+1]}')
elif minutes >= 45:
    if minutes == 49:
        print(f'без одной минуты {hours_dict1[hours+1]}')
    else:    
        print(f'без {minutes_dict4[60-minutes]} минут {hours_dict1[hours+1]}')
elif 30 < minutes < 45:
    if minutes == 40:
        print(f'{minutes_dict2[minutes//10]} минут {hours_dict2[hours+1]}')
    elif minutes%10 == 1:
        print(f'{minutes_dict2[minutes//10]} {minutes_dict1[minutes%10]} минута {hours_dict2[hours+1]}')
    elif 1 < minutes%10 <= 4:
        print(f'{minutes_dict2[minutes//10]} {minutes_dict1[minutes%10]} минуты {hours_dict2[hours+1]}')
>>>>>>> Stashed changes
    else:
        print(f'{minutes_dict2[minutes//10]} {minutes_dict1[minutes%10]} минут {hours_dict2[hours+1]}')
else:
    if 10 <= minutes <= 20:
        print(f'{minutes_dict3[minutes]} минут {hours_dict2[hours+1]}')
    elif minutes < 10:
<<<<<<< Updated upstream
        print(f'{minutes_dict1[minutes]} минут {hours_dict2[hours+1]}')
    else:
        print(f'{minutes_dict2[minutes//10]} {minutes_dict1[minutes%10]} минут {hours_dict2[hours+1]}')
=======
        if minutes == 1:   
            print(f'{minutes_dict1[minutes]} минута {hours_dict2[hours+1]}')
        elif 2 <= minutes <= 4:
            print(f'{minutes_dict1[minutes]} минуты {hours_dict2[hours+1]}')
        else:
            print(f'{minutes_dict1[minutes]} минут {hours_dict2[hours+1]}')
    else:
        if minutes%10 == 1:   
            print(f'{minutes_dict2[minutes//10]} {minutes_dict1[minutes%10]} минута {hours_dict2[hours+1]}')
        elif 2 <= minutes%10 <= 4:
            print(f'{minutes_dict2[minutes//10]} {minutes_dict1[minutes%10]} минуты {hours_dict2[hours+1]}')
        else:
            print(f'{minutes_dict2[minutes//10]} {minutes_dict1[minutes%10]} минут {hours_dict2[hours+1]}')
>>>>>>> Stashed changes
