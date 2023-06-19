import re

def enter():
    while True:
        str_length = input('Enter the desired string length (36 or more): \n')
        try:
            str_length = int(str_length)
            if str_length > 35:
                return str_length
            else:
                print('The input must be 36 or more\n')
        except ValueError:
            print('The input must be only integer. Please try again.\n')

str_lenght = enter()

with open('text.txt','r',encoding='utf-8') as f:
    text = f.read().split()

lines = []
new_line = ''

for word in text:
    word = word.rstrip()
    if len(new_line) + len(word) + 1 <= str_lenght + 1:
        new_line +=str(word) + " "
    else:
        lines.append(new_line.rstrip())
        new_line = str(word) + " "
lines.append(new_line.rstrip())

to_file = []

for line in lines:
    spaces = line.count(' ')
    difference = str_lenght - len(line)
    extra_spaces = difference - spaces
    if difference == 0:
        to_file.append(line)
    elif spaces == difference:
        line = re.sub(r' ','  ',line)
        to_file.append(line)
    elif spaces > difference:
        line = re.sub(' ','  ',line,count=difference)
        to_file.append(line)
    elif spaces < difference:
        line = re.sub(r' ','  ',line)
        line = re.sub(r' ', '  ', line,count=extra_spaces)
        if len(line) < str_lenght:
            difference = str_lenght - len(line)
            line = re.sub(r' ', '  ', line, count=difference)
        to_file.append(line)

with open('res_text.txt','w',encoding='utf-8') as n_f:
    for line in to_file:
        n_f.write(line+'\n')

print(f'Done! The name of new file with {str_lenght} characters per line is "res_text.txt" ')
