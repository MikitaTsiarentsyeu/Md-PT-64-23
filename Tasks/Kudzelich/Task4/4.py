while True:
    num = input("Enter a number greater 35, that equal to the maximum number of characters per line:\n")

    if not num.isdigit():
        print("Please, enter only digits")
        continue
    num = int(num)

    if not num > 35:
        print("Please, enter a number greater than 35")
        continue
    
    break

with open("text.txt", 'r', encoding='utf-8') as f:
    text = f.read().split()

new_line = ""
result = []
count = 0

for i in text:
    count += len(i)
    if count >= num:
        new_line += "\n"
        count = len(i)
    elif new_line != "":
        new_line += " "
        count +=1
    new_line += i

for j in new_line.split("\n"):
    num_space = num - len(j)
    while num_space > 0:
        j = j.replace(" ", "  ", num_space)
        num_space = num -  len(j)
    result.append(j+'\n')

with open ("new_text.txt", 'w', encoding='utf-8') as f:
    for i in result:
        f.write(i)
    
print(f"New text with", num, "characters per line is ready")