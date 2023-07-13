import os
p = os.path.join('Md-PT-64-23', 'Tasks', 'Korotkevich', 'Task6')
os.chdir(p)

import time

def create_file(func):
    def wrapper(*args):
        global time
        start = time.time()
        func(*args)
        finish = time.time()
        result = func(*args)
        time_p = finish - start
        with open('summ.txt', 'a') as f:
            f.write(f'Result - {result}, time - {time_p}, arguments - {args}\n')
    return wrapper

@create_file
def summ(a, b, c):
    return a*b*c

summ(11, 17, 24)
summ(12, 22, 31)
