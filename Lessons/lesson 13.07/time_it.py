import time

is_started = False

def start():
    global start_time
    global is_started
    is_started = True
    start_time = time.time()

def finish():
    if is_started:
        end = time.time()
        global is_started
        is_started = False
        return end - start_time