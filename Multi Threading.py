# Multi Tasking
from time import sleep
from threading import *

class hello(Thread):
    def run(self):
        for i in range(5):
            print('hello')
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print('hi')
            sleep(1)


obj1 = hello()
obj2 = hi()
obj1.start()
sleep(0.5)
obj2.start()

obj1.join()
obj2.join()
#obj1.start() Threads can only be started once
print('BYE it\'s the main thread bro')