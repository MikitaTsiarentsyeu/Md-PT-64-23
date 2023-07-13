#5. Write a function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers, check the example below:
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

def func(numbers):
    list = []
    first = numbers[0]
    last = numbers[0]

    for i in range (1, len(numbers)):
        if numbers[i]==last+1:
            last = numbers[i]
        else:
            if first==last:
                list.append(str(first))
            else:
                list.append(str(first) + '-'+str(last))
            first = numbers[i]
            last = numbers[i]
    if first == last:
        list.append(str(first))
    else:
        list.append(str(first) + '-' + str(last))
    return ', '.join(list)

numbers = [0,1,2,3,4,7,8,10]
res = func(numbers)
print(res)


