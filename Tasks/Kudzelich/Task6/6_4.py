import time

def decor(func):

    def inner(*args):
        start = time.time()
        value = func(*args) 
        end = time.time()
        execution_time = end - start

        with open ("result.txt", 'w', encoding='utf-8') as f:
            result = f"The execution time: {execution_time},\nArguments: {args},\nThe value of the function: {value}."
            f.write(result)

    return inner

@decor
def mult(*args):
    pr=1
    for i in args:
        pr*=i
    return pr

mult(1234, 5739, 8448, 6490)
print("the file 'result.txt' has been created")