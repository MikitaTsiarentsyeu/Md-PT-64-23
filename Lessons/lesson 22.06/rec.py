def level1():
    print("start of level 1")
    level2()
    print("end of level 1")

def level2():
    print(" start of level 2")
    level3()
    print(" end of level 2")

def level3():
    print("     start of level 3")
    level4()
    print("     end of level 3")

def level4():
    print("         start of level 4")
    print("         end of level 4")

# level1()

def level(i=1):
    if i == 5:
        return
    print(("\t"*i)+f"start of level {i}")
    level(i+1)
    print(("\t"*i)+f"end of level {i}")

level()


def print_n_times(text, n, counter=0):
    if counter == n:
        return
    print(text)
    print_n_times(text, n, counter+1)

print_n_times("recursion", 5)

for i in range(5):
    print("cycle")

structure = [1,2,[4,3,[3,3,5,7,[3,5,7,8],7,3],6],6,87,9]

sum = 0
for i in structure:
    print(i)
    if isinstance(i, list):
        for ii in i:
            print(ii)
            if isinstance(ii, list):
                for iii in ii:
                    print(iii)
                    if isinstance(iii, list):
                        for iiii in iii:
                            print(iiii)
                            sum += iiii
                    else:
                        sum += iii
            else:
                sum += ii
    else:
        sum += i

print(sum)

def flat_sum(l, sum=0):
    for i in l:
        if isinstance(i, int):
            sum += i
        else:
            sum += flat_sum(i, sum)
    
    return sum

print(flat_sum(structure))
