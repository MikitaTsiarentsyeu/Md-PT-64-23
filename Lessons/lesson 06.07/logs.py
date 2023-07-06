import time

def log(func):
    def wrapper(*args):
        print(f"{func.__name__}:")
        print("start!")
        start = time.time()
        result = func(*args)
        finish = time.time()
        print("finish!")
        t = finish-start
        print(t)
        return result
    return wrapper

@log
def target_func():
    print("something")

@log
def sum(a, b):
    return a+b

target_func()
result = sum(2, 3)
print(result*3)