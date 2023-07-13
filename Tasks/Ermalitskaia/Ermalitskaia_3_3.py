str1 = input()
str1 = str1.lower()
count = dict()
words = str1.split(' ')
for word in words:
    if word in count:
        count[word] = count[word] + 1
    else:
        count[word] = 1
for key in list(count.keys()):
    print(key, ":", count[key])
