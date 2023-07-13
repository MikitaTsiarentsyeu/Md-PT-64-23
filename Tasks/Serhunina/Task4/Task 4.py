import os
my_p = os.path.join('IT academy', 'My repo', 'Md-PT-64-23', 'Tasks', 'Serhunina','Task4')

user_input = int(input("Enter your value, maximum number of characters per line must be greater than 35\n"))

with open("text.txt", "r") as f:
    content = f.read()

content = content.split()

empty_line = ""
lines = []

for word in content:
    if len(empty_line) + len(word) < user_input:
        empty_line = word if len(empty_line) == 0 else empty_line + " " + word
        continue
    elif len(empty_line) == user_input:
        empty_line = empty_line + "\n"
        lines.append(empty_line)
        empty_line = ""
        continue


    missing_space = user_input - len(empty_line)
    count = empty_line.count(' ')

    ratio = missing_space//count
    leftover = missing_space%count
    spaces = ' '*(ratio+1)

    empty_line = empty_line.replace(' ', spaces)

    if leftover > 0:
        empty_line = empty_line.replace(spaces, f"{spaces} ", leftover)
    
    empty_line = empty_line+"\n"
    lines.append(empty_line)
    empty_line = word

with open("a_new1_test.txt", 'w') as f:
    f.writelines(lines)