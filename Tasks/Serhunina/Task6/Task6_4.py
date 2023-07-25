#Write a decorator function that logs the execution time, arguments and return value of a function to a file.
import time
def log_execution_time(func):
    def wrapper(*args):
        with open("log.txt", "a") as file:
            start_time = time.time()
            result = func(*args)
            execution_time = time.time() - start_time
            file.write(f"Function {func} executed with arguments {args} and returned {result} in {execution_time} seconds.\n")
        return result
    return wrapper

@log_execution_time
def sum_even_numbers(l):
    try:
        return sum(i for i in l if i % 2 == 0)
    except TypeError:
        return "Invalid input type"
print(sum_even_numbers([1, 2, 3, 4, 5, 6])) 
print(sum_even_numbers([7, 9, 0])) 
print(sum_even_numbers("str"))

