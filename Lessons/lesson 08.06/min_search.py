l = [436,32,34,7,65,4,23,4567,9,2]

print(min(l))

min_val = l[0]

isFirst = True
for item in l:
    if isFirst:
        isFirst = False
        continue
    if item < min_val:
        min_val = item

print(min_val)

min_i = 0
for i in range(1, len(l)):
    if l[i] < l[min_i]:
        min_i = i

print(min_i, l[min_i])