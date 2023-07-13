import time

def log(func):
    def wraper(*args):
        start = time.time()
        value = func(*args)
        end = time.time()
        res = start - end
        with open('log.txt','w',encoding='utf-8') as f:
            result = f'Execution time {res} seconds,\narguments {args},\nvalue of a function {value}' 
            f.write(result)
        return value
    return wraper

@log
def suma(a,b):
    result = a+b
    return result

suma(3,5)