limit = 35

with open("text.txt", "r") as f:
    content = f.read()

content = content.split()

current_line = ""
lines = []

for word in content:
    if len(current_line) + len(word) < limit:

        current_line = word if len(current_line) == 0 else current_line + " " + word
        continue
    elif len(current_line) == limit:
        current_line = current_line + "\n"
        lines.append(current_line)
        current_line = ""
        continue

    # current_line = current_line[:-1]
    miss = limit - len(current_line)
    count = current_line.count(' ')

    ratio = miss//count
    rem = miss%count
    spaces = ' '*(ratio+1)

    current_line = current_line.replace(' ', spaces)

    if rem > 0:
        current_line = current_line.replace(spaces, f"{spaces} ", rem)
    
    current_line = current_line+"\n"
    lines.append(current_line)
    current_line = word

with open("a_new_test.txt", 'w') as f:
    f.writelines(lines)