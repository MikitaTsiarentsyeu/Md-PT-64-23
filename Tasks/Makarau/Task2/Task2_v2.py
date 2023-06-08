time=input("Enter time in the format hh:mm\n")

if time.count(":") == 1:
    hh=time.split(":")[0]
    mm=time.split(":")[1]  
    if hh.isdigit() and mm.isdigit() and 0 <= int(hh) <= 23 and 0 <= int(mm) <= 59:
        hh=int(hh)
        mm=int(mm)
    else:
        print("You entered the wrong data format")
        exit()
else:
    print("You entered the wrong data format")
    exit()

if hh>12:
    hh=hh-12
else:
    hh=hh

time_dir = {
    0:["ноль","двенадцатого","ровно",""],
    1:["час","первого","одна","одной"],
    2:["два","второго","две","двух"],
    3:["три","третьего","","трех"],
    4:["четыре","четвертого","","четырех"],
    5:["пять","пятого","","пяти"],
    6:["шесть","шестого","","шести"],
    7:["семь","седьмого","","семи"],
    8:["восемь","восьмого","","восьми"],
    9:["девять","девятого","","девяти"],
    10:["десять","десятого","","десяти"],
    11:["одиннадцать","одиннадцатого","","одиннадцати"],
    12:["двенадцать","двенадцатого","","двенадцати"],
    13:["","","тринадцать","тринадцати"],
    14:["","","четырнадцать","четырнадцати"],
    15:["","","пятнадцать","пятнадцати"],
    16:["","","шестнадцать",""],
    17:["","","семнадцать",""],
    18:["","","восемнадцать",""],
    19:["","","девятнадцать",""],
    20:["","","двадцать",""],
    30:["","","тридцать","половина"],
    40:["","","сорок",""]
}

hours_tokens = ("часа","часов","без")
minuts_tokens = ("минута","минуты","минут")

if mm==0:
    if hh==1:
        print(f"{time} - {time_dir[hh][0]} {time_dir[0][2]}")
    elif 1<hh<=4:
        print(f"{time} - {time_dir[hh][0]} {hours_tokens[0]} {time_dir[0][2]}")       
    else:
        print(f"{time} - {time_dir[hh][0]} {hours_tokens[1]} {time_dir[0][2]}")

if hh==12:
    hh=0
else: 
    hh=hh

if mm<30:
    if mm==1:
        print(f"{time} - {time_dir[mm][2]} {minuts_tokens[0]} {time_dir[hh+1][1]} {hours_tokens[0]}")
    elif 1<mm<=4:
        if time_dir[mm][2]==(""):
            time_dir[mm][2]=time_dir[mm][0]
        print(f"{time} - {time_dir[mm][2]} {minuts_tokens[1]} {time_dir[hh+1][1]} {hours_tokens[0]}")
    elif 5<mm<=20:
        if time_dir[mm][2]==(""):
            time_dir[mm][2]=time_dir[mm][0]
        print(f"{time} - {time_dir[mm][2]} {minuts_tokens[2]} {time_dir[hh+1][1]} {hours_tokens[0]}")
    elif mm>20:
        if mm==21:
            print(f"{time} - {time_dir[20][2]} {time_dir[mm-20][2]} {minuts_tokens[0]} {time_dir[hh+1][1]} {hours_tokens[0]}")
        elif 21<mm<=24:
            print(f"{time} - {time_dir[20][2]} {time_dir[mm-20][2]} {minuts_tokens[1]} {time_dir[hh+1][1]} {hours_tokens[0]}")
        elif 24<mm:
            if time_dir[mm-20][2]==(""):
                time_dir[mm-20][2]=time_dir[mm-20][0]
            print(f"{time} - {time_dir[20][2]} {time_dir[mm-20][2]} {minuts_tokens[2]} {time_dir[hh+1][1]} {hours_tokens[0]}")

elif mm==30:
    print(f"{time} - {time_dir[mm][3]} {time_dir[hh+1][1]} {hours_tokens[0]} ")
    
elif 30<mm<45:
    if mm-(mm//10*10)==1:
        print(f"{time} - {time_dir[mm//10*10][2]} {time_dir[mm-(mm//10*10)][2]} {minuts_tokens[0]} {time_dir[hh+1][1]} {hours_tokens[0]}")      
    elif 1<mm-(mm//10*10)<=4:
        if time_dir[mm-(mm//10*10)][2]==(""):
            time_dir[mm-(mm//10*10)][2]=time_dir[mm-(mm//10*10)][0]
        print(f"{time} - {time_dir[mm//10*10][2]} {time_dir[mm-(mm//10*10)][2]} {minuts_tokens[1]} {time_dir[hh+1][1]} {hours_tokens[0]}")
    elif 4<mm-(mm//10*10)<=9:
        if time_dir[mm-(mm//10*10)][2]==(""):
            time_dir[mm-(mm//10*10)][2]=time_dir[mm-(mm//10*10)][0]
        print(f"{time} - {time_dir[mm//10*10][2]} {time_dir[mm-(mm//10*10)][2]} {minuts_tokens[2]} {time_dir[hh+1][1]} {hours_tokens[0]}")
    elif mm==40:
        print(f"{time} - {time_dir[mm][2]} {minuts_tokens[2]} {time_dir[hh+1][1]} {hours_tokens[0]}") 
elif mm>= 45:
    print(f"{time} - {hours_tokens[2]} {time_dir[60-mm][3]} {minuts_tokens[2]} {time_dir[hh+1][1]} {hours_tokens[0]} ")