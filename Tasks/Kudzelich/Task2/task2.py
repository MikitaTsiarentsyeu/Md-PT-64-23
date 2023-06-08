dict_hours = {
        "0": ["двенадцать", "двенадцатого", "часов"],
        "1": ["один", "первого", "час"],
        "2": ["два", "второго", "часа"],
        "3": ["три", "третьего", "часа"],
        "4": ["четыре", "четвёртого", "часа"],
        "5": ["пять", "пятого", "часов"],
        "6": ["шесть", "шестого", "часов"],
        "7": ["семь", "седьмого", "часов"],
        "8": ["восемь", "восьмого", "часов"],
        "9": ["девять", "девятого", "часов"],
        "10": ["десять", "десятого", "часов"],
        "11": ["одиннадцать", "одиннадцатого", "часов"],
        "12": ["двенадцать", "двенадцатого", "часов"],
        }

dict_minutes = {
        "0": ["ноль", "ровно"],
        "1": ["одна", "одной"],
        "2": ["две", "двух"],
        "3": ["три", "трёх"],
        "4": ["четыре", "четырёх"],
        "5": ["пять", "пяти"],
        "6": ["шесть", "шести"],
        "7": ["семь", "семи"],
        "8": ["восемь", "восьми"],
        "9": ["девять", "девяти"],
        "10": ["десять", "десяти"],
        "11": ["одиннадцать", "одиннадцати"],
        "12": ["двенадцать", "двенадцати"],
        "13": ["тринадцать", "тринадцати"],
        "14": ["четырнадцать", "четырнадцати"],
        "15": ["пятнадцать", "пятнадцати"],
        "16": ["шестнадцать"],
        "17": ["семнадцать"],
        "18": ["восемнадцать"],
        "19": ["девятнадцать"],
        "20": ["двадцать"],
        "30": ["тридцать", "половина"],
        "40": ["сорок"]
        }

minutes_tokens = ["минут", "минута", "минуты"]


try:
    time = input("Enter data in the format hh:mm:\n")
    hh = int(time[0:2])
    mm = int(time[3:5])
    mm_1 = time[3:4]+"0" #the first symbol in seconds
    mm_2 = time[4:5] #the second symbol in seconds
    if not (0 <= hh <= 24 and 0 <= mm <=59 and time[2:3] == ":" and len(time) == 5) or (hh == 24 and mm > 0):
        print("You enter a wrong data")
        exit()

except ValueError:
    print("You enter a wrong data")
    exit()


if hh >= 12:
    hh -= 12

# the condition for adding the word "minute"
if mm == 1 or (mm > 20 and mm % 10 == 1):
    minute_token = minutes_tokens[1]
elif mm in (2,3,4) or (mm > 20 and mm % 10 in (2,3,4)):
    minute_token = minutes_tokens[2]
else:
    minute_token = minutes_tokens[0]


# the main condition
if mm == 0:
    print(dict_hours[f"{hh}"][0], dict_hours[f"{hh}"][2], dict_minutes[f"{mm}"][1])

elif mm < 30:
    if mm > 20:
        print(dict_minutes[f"{mm_1}"][0], dict_minutes[f"{mm_2}"][0], minute_token, dict_hours[f"{hh+1}"][1])
    else:
        print(dict_minutes[f"{mm}"][0], minute_token, dict_hours[f"{hh+1}"][1])

elif mm == 30:
    print(dict_minutes[f"{mm}"][1], dict_hours[f"{hh+1}"][1])

elif 30 < mm < 45:
    if mm == 40:
         print(dict_minutes[f"{mm}"][0], minute_token, dict_hours[f"{hh+1}"][1])
    else:
        print(dict_minutes[f"{mm_1}"][0], dict_minutes[f"{mm_2}"][0], minute_token, dict_hours[f"{hh+1}"][1])

elif mm >= 45:
    if 60 - mm == 1:
        minute_token = minutes_tokens[2]
        print("без", dict_minutes[f"{60-mm}"][1], minute_token, dict_hours[f"{hh+1}"][0])
    else:
        minute_token = minutes_tokens[0]
        print("без", dict_minutes[f"{60-mm}"][1], minute_token, dict_hours[f"{hh+1}"][0])

