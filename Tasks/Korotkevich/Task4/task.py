import os
p = os.path.join('Md-PT-64-23', 'Tasks', 'Korotkevich', 'Task4')
os.chdir(p)

flag = False
while flag == False:
    length = input('Please enter the maximum num_space of characters per line, which must be greater than 35: ')
    if length.isdigit() == True and int(length) > 35:
        length = int(length)
        flag = True
    else:
        print('Incorrect data. Try again.')

with open('text.txt', 'r') as f:
    text = f.read()
text = text.replace('\n', ' ')
text = text.split(' ')

line = ''
counter = 0
final = []

for i in text:
    counter += len(i)
    if counter >= length:
        line += "\n"
        counter = len(i)
    elif line != '':
        line += ' '
        counter += 1
    line += i
for j in line.split("\n"):
    num_space = length - len(j)
    while num_space > 0:
        j = j.replace(' ','  ', num_space)
        num_space = length - len(j)
    final.append(j+'\n')
with open('new_text.txt', 'w+') as f:
    for k in final:
        f.write(k)
