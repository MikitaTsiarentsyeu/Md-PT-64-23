a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [1, 2, 3, 'abc', 5, 6, 7, 8, 9, 10]

def my_sum (i):
    try:             
        my_list = list(filter(lambda x: x%2==0, i))
        return print(sum(my_list))
    except TypeError:
        print("Invalid input type")

my_sum(a)
my_sum(b)