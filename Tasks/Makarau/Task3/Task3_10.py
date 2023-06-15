list = input("Enter a list of numbers separated by spaces: ").split()
new_list = [int(x) for x in list]
l =[]
for i in new_list:
    for j in range(2,i):
        if i % j == 0:
         break
    else:
       l.append(i)
print(l)