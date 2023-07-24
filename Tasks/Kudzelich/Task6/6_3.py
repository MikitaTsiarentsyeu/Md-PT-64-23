def sum_even_nums(l, sum=0):
    try:
        if isinstance(l, list) == False:
            raise TypeError("The input is not a list")
        
        for i in l:
            if isinstance(i, int) == False:
                raise TypeError("Not every element is int")
            else:
                if i%2 == 0:
                    sum += i
        return f"The sum of even numbers is {sum}"                    
                
    except TypeError as er:
        return er

print(sum_even_nums([1,2,3,4]))
print(sum_even_nums("1,2,3,4"))
print(sum_even_nums([1,"2",3,4]))
print(sum_even_nums((1,2,3,4)))
print(sum_even_nums([2,4,6,7,9,10]))