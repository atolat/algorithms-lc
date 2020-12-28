from threading import *

# Create a thread without using any class
def display():
    for _ in range(1, 11):
        print("Child Thread")

t = Thread(target = display)  # creating Thread object
t.start()

for i in range(1, 11):
    print("Main Thread")

# Creating a thread by extending thread class
class MyThread(Thread):
    def run(self):
        for _ in range(10):
            print("Child Thread-1")


t = MyThread()
t.start()
for i in range(10):
    print("Main Thread-1")

# Creating a thread without extending thread class
class Test:
    def display(self):
        for _ in range(10):
            print("Child Thread-2")

obj = Test()
t = Thread(target = obj.display)
t.start()
for _ in range(10):
    print("Main Thread-2")
