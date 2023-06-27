def character_count(line):
    a = 0
    b = 0
    for i in line:
        if i.isupper():
            a +=1
        elif i.islower():
            b +=1
    return a,b
print(character_count(input("Enter line: ")))