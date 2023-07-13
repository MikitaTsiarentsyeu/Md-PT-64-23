with open('text.txt', 'r') as f:
    lines = f.readlines()
result =[]
num = int(input("Enter maximum number of characters per line (should be more than 35): \n"))
for j in range(len(lines)):
    words = lines[j].split(" ")
    list1 = []
    for i in range(len(words)):
        list1.append(words[i])
        if len(" ".join(list1)) == num:
            result.append(" ".join(list1))
            list1 = []
        if len(" ".join(list1)) > num:
           for l in range(1,10):
                if len(" ".join(list1[0:len(list1) - 1])) == num:
                    break
                for k in range(0, len(list1[0:len(list1)-2])):
                    list1[k] = list1[k] + " "
                    if len(" ".join(list1[0:len(list1)-1])) == num:
                        break
           result.append(" ".join(list1[0:len(list1) - 1]))
           list1 = []
           list1.append(words[i])
result.append(" ".join(list1))
r = "\n".join(result)
with open('text_a.txt', 'w') as res:
    res.writelines(r)
    res.close()


#print(r)
