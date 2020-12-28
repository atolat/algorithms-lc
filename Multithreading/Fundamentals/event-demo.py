from threading import *
import time
def trafficSignal():
    while True:
        time.sleep(10)
        print("GREEN")
        event.set()
        time.sleep(20)
        print("RED")
        event.clear()
        
def driver():
    num=0
    while True:
        print("Drivers waiting for GREEN Signal")
        event.wait()
        print("GREEN...Drivers can pass")
        while event.isSet():
            num += 1
            print("Vehicle No: ",num,)
            time.sleep(2)
        print("RED...Drivers have to STOP")

event=Event()
t1=Thread(target = trafficSignal)
t2=Thread(target = driver)
t1.start()
t2.start()