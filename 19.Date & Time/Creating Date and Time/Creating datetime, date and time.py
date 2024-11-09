# python program to implement datetime module (classes : datetime, date, time)

import datetime

# datetime module - datetime class

dt1 = datetime.datetime(2010, 1, 1, 10, 10, 10)
print(dt1)
# Output : datetime.datetime(2010, 1, 1, 10, 10, 10)

dt2 = datetime.datetime(2011, 1, 1, 10, 10, 10)
print(dt2)
# Output : datetime.datetime(2011, 1, 1, 10, 10, 10)

print(dt2 - dt1)
# Output : datetime.timedelta(days=365)

print(dt2 > dt1)
# Output : True

print(dt2 < dt1)
# Output : False

dt3 = datetime.datetime(day=1, month=1, year=2020, hour=10, minute=10, second=10)
print(dt3)
# Output : datetime.datetime(2020, 1, 1, 10, 10, 10)

print(dt3)
# Output : 2020-01-01 10:10:10



# datetime module - date class

date1 = datetime.date(2010, 1, 1)
print(date1)
# Output : datetime.date(2010, 1, 1)

date2 = datetime.date(2011, 1, 1)
print(date2)
# Output : datetime.date(2011, 1, 1)

print(date2 - date1)
# Output : datetime.timedelta(days=365)

print(date2 > date1)
# Output : True

print(date2 < date1)
# Output : False



# datetime module - time class

time1 = datetime.time(10, 10, 10)
print(time1)
# Output : datetime.time(10, 10, 10)

time2 = datetime.time(11, 11, 11)
print(time2)
# Output : datetime.time(11, 11, 11)

'''print(time2 - time1)
Output : Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'datetime.time' and 'datetime.time'
'''
print(time2 > time1)
# Output : True

print(time2 < time1)
# Output : False

# combine - static method - datetime.datetime class
dt3 = datetime.datetime.combine(date1, time1)

print(dt3)
# Output : 2010-01-01 10:10:10