import re
import datetime

def converter(l, s1):
    """A function that implements a text output of the time"""
    hour = int(l[0])
    minute = int(l[1])
    dict_time = {0:['первого', 'час', 'двенадцать часов', "", ""],
            1:['второго', 'два', 'один час', 'одна минута', 'одной минуты'],
            2:['третьего', 'три', 'два часа', 'две минуты', 'двух минут'],
            3:['четвёртого', 'четыри', 'три часа', 'три минуты', 'трех минут'],
            4:['пятого', 'пять', 'четыри часа', 'четыри минуты', 'четырех минут'],
            5:['шестого', 'шесть', 'пять часов', 'пять минут', 'пяти минут'],
            6:['седьмого', 'семь', 'шесть часов', 'шесть минут', 'шести минут'],
            7:['восьмого', 'восемь', 'семь часов', 'семь минут', 'семи минут'],
            8:['девятого', 'девять', 'восемь часов', 'восемь минут', 'восеми минут'],
            9:['десятого', 'десять', 'девять часов', 'девять минут', 'девяти минут'],
            10:['одиннадцатого', 'одиннадцать', 'десять часов', 'десять минут', 'десяти минут'],
            11:['двенадцатого', 'двенадцать', 'одиннадцать часов', 'одиннадцать минут', 'одиннадцати минут'],
            12:['первого', 'час', 'двенадцать часов', 'двенадцать минут', 'двенадцати минут'],
            13:['', '', '', 'тринадцать минут', 'тринадцати минут'],
            14:['', '', '', 'четырнадцать минут', 'четырнадцати минут'],
            15:['', '', '', 'пятнадцать минут', 'пятнадцати минут'],
            16:['', '', '', 'шестнадцать минут', ''],
            17:['', '', '', 'семнадцать минут', ''],
            18:['', '', '', 'восемнадцать минут', ''],
            19:['', '', '', 'девятнадцать минут', ''],
            20:['', '', '', 'двадцать', ''],
            30:['', '', '', 'тридцать', ''],
            40:['', '', '', 'сорок', ''],}
    if hour <= 12:
        if minute == 0:
            res = (f'{s1} - {dict_time[hour][2]} ровно')
        elif minute < 20:
            res = (f'{s1} - {dict_time[minute][3]} {dict_time[hour][0]}')
        elif minute == 20:
            res = (f'{s1} - {dict_time[20][3]} минут {dict_time[hour][0]}')    
        elif minute < 30:
            res = (f'{s1} - {dict_time[20][3]} {dict_time[(minute-20)][3]} {dict_time[hour][0]}')
        elif minute == 30:
            res = (f'{s1} - половина {dict_time[hour][0]}')
        elif minute < 40:
            res = (f'{s1} - {dict_time[30][3]} {dict_time[(minute-30)][3]} {dict_time[hour][0]}')
        elif minute == 40:
            res = (f'{s1} - {dict_time[40][3]} минут {dict_time[hour][0]}') 
        elif minute < 45:
            res = (f'{s1} - {dict_time[40][3]} {dict_time[(minute-40)][3]} {dict_time[hour][0]}')
        elif minute >= 45:
            res = (f'{s1} - без {dict_time[(60-minute)][4]} {dict_time[hour][1]}')
        return res    
    else:
        l[0] = int(l[0]) - 12
        res = converter(l, s1)
        return res

def time_now():
    current_date_time = datetime.datetime.now()
    current_time = current_date_time.time()
    return current_time

errors = {1:'Check Quantity : - colon', 
        2:'Input must contain: hour - two characters, : -colon character, minute - two characters!',
        3:'Input must contain only numbers and colon'
        }

if __name__ == "__main__":
    number = int(input("Hello, please select:\n 1.Display the current time \n 2.Set your time \n 3.Exiting the program\n"))
    if number == 1:
        result = time_now()
        print(result)
    elif number == 2:
        time = input('Enter time in hh:mm format\n')
        check_colon = re.findall(':', time)
        if len(check_colon) == 1:
            h_m = time.split(':')
            if len(h_m[0]) <= 2 and len(h_m[0]) <= 2:
                if h_m[0].isdigit()==True and h_m[1].isdigit()==True:
                    result = converter(h_m, time)
                    print(result)
                else:
                    print(errors[3])
            else:
                print(errors[2])
        else:
            print(errors[1])
    elif number == 3:
        print('Good bye')
        exit()


