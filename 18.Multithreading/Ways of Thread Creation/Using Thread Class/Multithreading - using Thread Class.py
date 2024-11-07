# python program to implement multithreading using Thread class

from threading import *
from time import *

# external thread
class Alphabets(Thread):
    
    def run(self):
        for i in range(65, 91):
            print(chr(i))
            sleep(1)

# external thread
a = Alphabets()

a.start()   # to run (or) execute a thread

# main thread (or) main program 
for i in range(65, 91):
    print(i)
    sleep(1)

a.join()    # to make the main program wait for the thread to complete its execution