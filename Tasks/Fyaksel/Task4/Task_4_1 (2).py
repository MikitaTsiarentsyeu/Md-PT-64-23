# _*_ utf-8 _*_

import re

def fam():
    while True:
        s_len = input('Input the desired string length (36 or more): \n')
        try:
            s_len = int(s_len)
            if s_len > 35:
                return s_len
            else:
                print('The input must be 36 or more\n')
        except ValueError:
            print('The input must be only integer. Please try again.\n')

s_len = fam()

with open('text.txt','r',encoding='utf-8') as f:
    text = f.read().split()

lines = []
new_line = ''

for word in text:
    word = word.rstrip()
    if len(new_line) + len(word) + 1 <= s_len + 1:
        new_line +=str(word) + " "
    else:
        lines.append(new_line.rstrip())
        new_line = str(word) + " "
lines.append(new_line.rstrip())

to_file = []

for line in lines:
    spaces = line.count(' ')
    difference = s_len - len(line)
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
        if len(line) < s_len:
            difference = s_len - len(line)
            line = re.sub(r' ', '  ', line, count=difference)
        to_file.append(line)

with open('res_text.txt','w',encoding='utf-8') as n_f:
    for line in to_file:
        n_f.write(line+'\n')

print(f'The name of new file with {s_len} characters per line is "example_40_symbols" ')
