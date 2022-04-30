from threading import Thread
import time

def func():
    print("sleeping for 10 second")
    time.sleep(10)
    print("sleep is over")
print("calling function")
t = Thread(target=func)
t.start()
print("function is calling")
