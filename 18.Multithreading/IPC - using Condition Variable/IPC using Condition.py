# python program to implement inter process communication - using condition variable - through producer consumer problem

from threading import *
from time import *

# class for shared data
class SharedData:
    
    def __init__(self):
        self.data = 0
        self.condition_variable = Condition()
    
    # method for putting data into shared data 
    def put(self, x):
        self.condition_variable.acquire()
        self.condition_variable.wait(timeout=0)
        self.data = x   # writing data
        self.condition_variable.notify()
        self.condition_variable.release()
        sleep(1)
    
    # method for getting data from shared data
    def get(self):
        self.condition_variable.acquire()
        self.condition_variable.wait(timeout=0)
        x = self.data   # reading data
        self.condition_variable.notify()
        self.condition_variable.release()
        sleep(1)
        
        return x

# function used for creating a thread
def producer(data):
    i = 1
    
    while True:
        data.put(i)
        print('Producer :', i)
        i += 1

# function used for creating a thread
def consumer(data):
    while True:
        x = data.get()
        print('Consumer :', x)

# creating object for SharedData class
data = SharedData()

# creating 2 threads from 2 functions producer and consumer
t1 = Thread(target=lambda : producer(data))
t2 = Thread(target=lambda : consumer(data))

t1.start()
t2.start()

t1.join()
t2.join()