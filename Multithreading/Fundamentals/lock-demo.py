from threading import *
import time

# Create Lock
l = Lock()

def greet(name):
    l.acquire()
    # Critical Section
    for _ in range(10):
        print("Good Evening:", flush=True, end='')
        time.sleep(2)
        print(name)
    l.release()

# Only one thread can acquire the lock and execute the code in critical section
t1 = Thread(target=greet, args=("A",))
t2 = Thread(target=greet, args=("B",))
t3 = Thread(target=greet, args=("C",))
t1.start()
t2.start()
t3.start()
