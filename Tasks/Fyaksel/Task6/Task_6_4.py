# Write a decorator function that logs the execution time, arguments and return value of a function to a file.

import time

def decor(func):

    def inner(*args):
        start = time.time()
        value = func(*args) 
        end = time.time()
        execution_time = end - start

        with open ("save.txt", 'w', encoding='utf-8') as f:
            result = f"The execution time: {execution_time},\nArguments: {args},\nThe value of the function: {value}."
            f.write(result)

    return inner

@decor
def mult(*args):
    pr=1
    for i in args:
        pr*=i
    return pr

mult(7755, 1805, 3475, 3277)
print("the file 'save.txt' has been created")