# python program to implement formatting in date and time

from datetime import *

# strftime method - classes (datetime, date, time)
dt1 = datetime(2010, 1, 1, 10, 20, 30)
print(dt1)
# Output : datetime.datetime(2010, 1, 1, 10, 20, 30)

print(dt1.strftime('%d %B %Y, %H:%M:%S'))
# Output : '01 January 2010, 10:20:30'

'''print(dt1.strftime('%-d %B %Y, %H:%M:%S'))
# Output : Traceback (most recent call last):

  File "<stdin>", line 1, in <module>
ValueError: Invalid format string'''



# strptime method - classes (datetime)

str1 = '10 January 2015, 10:15:30'

dt2 = datetime.strptime(str1, '%d %B %Y, %H:%M:%S')
print(dt2)
# Output : datetime.datetime(2015, 1, 10, 10, 15, 30)

print(dt2)
# Output : 2015-01-10 10:15:30

print(type(str1))
# Output : <class 'str'>

print(type(dt2))
# Output : <class 'datetime.datetime'>