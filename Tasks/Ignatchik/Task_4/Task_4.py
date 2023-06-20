while True:
    num = input('Enter the "maximum number of characters per line" parameter, which must be greater than 35:\n')
    if num.isdigit() != True:
        print('wrong enter')
        continue
    elif int(num) <= 35:
        print('wrong enter')
        continue
    break

enter = int(num)
with open('text.txt', 'r', encoding='utf-8') as file:
    word_list = (file.read()).split()
new_line = ''
count = 0
res = []
for i in word_list:
    count += len(i)
    if count >= enter:
        new_line += "\n"
        count = len(i)
    elif new_line != '':
        new_line += ' '
        count += 1
    new_line += i        
for j in new_line.split("\n"):
    number = enter - len(j)
    while number > 0:
        j = j.replace(' ','  ', number)
        number = enter - len(j)
    res.append(j+'\n')
with open('new_text.txt', 'w', encoding='utf-8') as file:
    for k in res:
        file.write(k)
    print('The new file "new_text.txt" has been written, taking into account the entered parameters')