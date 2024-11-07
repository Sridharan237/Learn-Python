# python program to implement mutex in multithreading

from threading import *
from time import *

# function used for running inside a thread - function that prints each character from passed parameter string
def display(str1):
    l.acquire()
    for ch in str1:
        print(ch)
        sleep(0.1)
    l.release()
        
l = Lock()  # to create a lock

# external threads
t1 = Thread(target=display, args=('HELLO WORLD',))
t2 = Thread(target=display, args=('you are welcome', ))

t1.start()  
t2.start()

t1.join()   
t2.join()