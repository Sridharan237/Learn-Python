# python program to implement multithreading using function / method

from threading import *
from time import *

# external thread
def display():
    for i in range(65, 91):
        print(chr(i))
        sleep(1)
        
# external thread
t = Thread(target=display, name='Alphabets')

t.start()   # to run (or) execute a thread

# main thread (or) main program
for i in range(65, 91):
    print(i)
    sleep(1)

t.join()    # to make the main program wait for the thread to complete its execution