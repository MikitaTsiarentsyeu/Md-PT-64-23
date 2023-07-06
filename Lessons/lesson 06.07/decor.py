import time

def show_text():
    time.sleep(1)
    print("some text")

def test_func():
    print("test")

def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper

# def twice_show_text():
#     show_text()
#     show_text()

twice_show_text = do_twice(show_text)

twice_show_text()

twice_test_func = do_twice(test_func)

twice_test_func()

def time_it(func):
    def wrapper():
        start = time.time()
        func()
        finish = time.time()
        print(finish - start)
    return wrapper

# time_it_show_text = time_it(show_text)
time_it_show_text = time_it(twice_show_text)
time_it_show_text()

time_it_show_text = do_twice(time_it(show_text))
time_it_show_text()


def cheap_trick(func):
    def wrapper():
        print("it's just smoke and mirrors")
        func()
    return wrapper

@cheap_trick
def target_func():
    print("something very important")

print("some logic")

# target_func = cheap_trick(target_func)

target_func()