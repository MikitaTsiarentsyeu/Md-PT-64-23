import time

def timer(t, callback, text):
    time.sleep(t)
    callback(text)

def show_text(text):
    print(text)

timer(2, show_text, "new text")