# python program to implement semaphore in multithreading

from threading import *
from time import *

# function used for running inside a thread - function that prints each character from passed parameter string
def display(str1):
    s.acquire()
    
    for ch in str1:
        print(ch)
        sleep(0.1)
        
    s.release()
        
s = Semaphore(2)  # to create a semaphore - to run 2 threads at the same time and lock it

# external threads
t1 = Thread(target=display, args=('HELLO WORLD',))
t2 = Thread(target=display, args=('you are welcome', ))
t3 = Thread(target=display, args=('1234567890',))

t1.start()  
t2.start()
t3.start()

t1.join()   
t2.join()
t3.join()