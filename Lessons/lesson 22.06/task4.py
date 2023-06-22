limit = 35

with open("test.txt", "r") as f:
    content = f.read()

content = content.split()

current_line = ""
lines = []

for word in content:
    if len(current_line) + len(word) < limit:

        current_line = current_line + word + " "
        continue
    elif len(current_line) == limit:
        current_line = current_line[:-2]+"\n"
        lines.append(current_line)
        current_line = ""
        continue

    miss = limit - len(current_line)
    count = current_line.count(' ')

    ratio = miss//count
    rem = miss%count
    spaces = ' '*(ratio+1)

    current_line = current_line.replace(' ', spaces)

    if rem > 0:
        current_line = current_line.replace(spaces, f"{spaces} ", rem)
    
    current_line = current_line[:-2]+"\n"
    lines.append(current_line)
    current_line = ""

with open("new_test.txt", 'w') as f:
    f.writelines(lines)
