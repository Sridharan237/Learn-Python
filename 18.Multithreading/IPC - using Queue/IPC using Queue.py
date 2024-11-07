# python program to implement IPC (Inter Process Communication) - using Queue

from threading import *
from time import *
from queue import Queue

# function used for creating a thread
def producer(queue):
    i = 1
    
    while True:
        queue.put(i)
        print('Producer :', i)
        sleep(1)
        i += 1

# function used for creating a thread
def consumer(queue):
    while True:
        x = queue.get()
        print('Consumer :', x)
        sleep(1)

# creating object for Queue class
q = Queue()

# creating 2 threads from 2 functions producer and consumer
t1 = Thread(target=lambda : producer(q))
t2 = Thread(target=lambda : consumer(q))

t1.start()
t2.start()

t1.join()
t2.join()