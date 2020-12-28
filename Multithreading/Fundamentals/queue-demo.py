from threading import *
import time
import random
import queue

def produce(q):
    while True:
        item = random.randint(1, 100)
        print("Producer Producing Item:", item)
        q.put(item)
        print("Producer Notifying")
        time.sleep(5)


def consume(q):
    while True:
        print("Consumer waiting")
        print("Consumer consuming the item:", q.get())
        time.sleep(5)


q = queue.Queue()
t1 = Thread(target=consume, args=(q,))
t2 = Thread(target=produce, args=(q,))
t1.start()
t2.start()
