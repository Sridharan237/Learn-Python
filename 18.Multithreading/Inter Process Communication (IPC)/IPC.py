# python program to implement inter process communication - shared data - through producer consumer problem

from threading import *
from time import *

# class for shared data
class SharedData:
    
    def __init__(self):
        self.data = 0
        self.flag = False
        self.lock = Lock()
    
    # method for putting data into shared data 
    def put(self, x):
        while self.flag != False:
            pass
        
        self.lock.acquire()
        self.data = x
        self.flag = True
        self.lock.release()
        sleep(1)
    
    # method for getting data from shared data
    def get(self):
        while self.flag != True:
            pass
        
        self.lock.acquire()
        x = self.data
        self.flag = False
        self.lock.release()
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