import time

def time_check (func):
    def wrapper (*args):
        start = time.time()
        res = func(*args)
        execution_time = time.time()-start         
        result = f"Execution time {execution_time} seconds.\nArguments {args}.\nValue of a function {res}."
        with open('Task6_4.txt', 'w+') as f:
            f.write(result)
        return res
    return wrapper
            
@time_check
def degree (a, b):
    return a**b

degree (2, 100)