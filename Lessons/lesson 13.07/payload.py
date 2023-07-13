import time_it
import timeit

def func():
    time_it.start()
    for i in range(100000):
        i+1
    print(time_it.finish())



print(timeit.timeit("[i for i in range(100)]"))