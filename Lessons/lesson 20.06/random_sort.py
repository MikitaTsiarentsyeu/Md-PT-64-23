import random

l = [3,5,6,8,65,8,1,2]

# res = sorted(l)
# print(res, l)

# res = l.sort()
# print(res, l)

def is_sorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def generate_index(n):
    return random.randint(0, n-1)

def swap(l, i, j):
    l[i], l[j] = l[j], l[i]

def random_sort(l):
    counter = 0
    while not is_sorted(l):
        i = generate_index(len(l))
        j = i
        while i == j:
            j = generate_index(len(l))
        swap(l, i, j)
        counter += 1
        
    return counter

print(random_sort(l))
print(l)