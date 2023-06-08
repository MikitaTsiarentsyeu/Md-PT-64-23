l = [6,4,2,4,7,9,9,5,3,2,1]

sorted_l = sorted(l)
print(sorted_l, l)

l.sort()
print(l)

print(sorted("abc AAC aaa".split()))

l = [6,4,2,4,7,9,9,5,3,2,1]

# counter = 0

# for j in range(len(l)-1):
#     for i in range(len(l)-1):
#         counter += 1
#         if l[i] > l[i+1]:
#             l[i], l[i+1] = l[i+1], l[i]
#     print(l)

# print(l)
# print(counter)

counter = 0

for j in range(len(l)-1):
    min_i = j
    for i in range(j+1, len(l)):
        counter += 1
        if l[i] < l[min_i]:
            min_i = i
    l[j], l[min_i] = l[min_i], l[j]

print(l)
print(counter)
