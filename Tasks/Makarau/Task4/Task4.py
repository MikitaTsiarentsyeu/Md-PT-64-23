width = int(input("Enter the maximum integer number of characters in the string, which must be greater than 35:"))

with open("text.txt", "r") as f:
    words=f.read().split()
    line = ""
    index = 0
    new_line = []

for i in words:
    index+=len(i)
    if index>=width:
        line += "\n"
        index=len(i)
    elif line != "":
        line += " "
        index +=1
    line +=i

for j in line.split("\n"):
    spaces = width - len(j)
    while spaces > 0:
        j = j.replace(" ","  ",spaces)
        spaces = width - len(j)
    new_line.append(j + "\n")  

with open ("new_text.txt", "w") as f:
    for i in new_line:
        f.write(i)