def sum_even_nums(lst):
    try:
        if isinstance(lst, list) == False:
            raise TypeError("Invalid input type. The input is not a list")

        if all(isinstance(i, int) for i in lst) == True:
            return sum(i for i in lst if i%2 == 0)
        else:
            raise TypeError("Invalid input type. Not every element is int")


    except TypeError as er:
        return er
    
print(sum_even_nums([1,2,3,4,5]))
print(sum_even_nums([1,3,5,7]))
print(sum_even_nums([1,2,3,"4"]))
print(sum_even_nums([1,2,3,"test"]))
print(sum_even_nums("test"))
