def even_numbers_sum(list1):
    sum1 = 0
    try:
        for i in list1:
            if isinstance(i, int) == False:
                return TypeError("Invalid input type")
            else:
                if i % 2 == 0:
                    sum1 = sum1 + i
        return f"The sum of even numbers is {sum1}"

    except TypeError as error1:
        return error1

print(even_numbers_sum([17,27,37,47]))
print(even_numbers_sum([18,28,38,48]))
print(even_numbers_sum([1.8,2.8,3.8,4.8]))