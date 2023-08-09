#Write a decorator function that logs the execution time, arguments and return value of a function to a file.

import time
import math

def execution_time(function1):
    def inner_function(*args):
        start_time = time.time()
        function_value = function1(*args)
        end_time = time.time()
        execution_time = end_time - start_time
        with open ("text_6_4.txt", 'w') as f:
            result = f"The execution time: {execution_time},\nArguments: {args},\nThe value of the function: {function_value}."
            f.write(result)
    return inner_function

@execution_time
def factorial_sum(x, y):
    return math.factorial(x) + math.factorial(y)

factorial_sum(3, 5)