numbers = input('Enter list of numbers to find prime numbers:\n').replace(',','').split(' ')

primes = []

for i in numbers:
    check_list =[x for x in range(2,int(i)+1)]
    deviders =[]
    for x in check_list:
        if int(i)%x == 0:
            deviders.append(x)
    if len(deviders) == 1:
        primes.append(i)

print(f'The largest prime number: {max(primes)}')