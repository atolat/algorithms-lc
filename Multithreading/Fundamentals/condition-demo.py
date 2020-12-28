from threading import *
import time
import random
items = []


def produce(c):
    while True:
        c.acquire()
        item = random.randint(1, 100)
        print("Producer Producing Item:", item)
        items.append(item)
        print("Producer Notifying Consumers...")
        c.notify()
        c.release()
        time.sleep(5)


def consume(c):
    while True:
        c.acquire()
        print("Consumer waiting for update")
        c.wait()
        print("Consumer consuming the item", items.pop())
        c.release()
        time.sleep(5)


c = Condition()
t1 = Thread(target=consume, args=(c,))
t = Thread(target=produce, args=(c,))
t1.start()
t .start()
