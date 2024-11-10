# python program to find the time taken for execution of code

from time import time

start_time = time()

# sample code
for i in range(0, 100000000):
    pass

end_time = time()

execution_time = end_time - start_time

print('Time taken for code execution : %.2f seconds' % execution_time)

print(type(execution_time))
# Output : <class 'float'>