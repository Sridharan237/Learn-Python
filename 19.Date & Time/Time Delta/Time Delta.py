# python program to implement the methods in timedelta class of datetime module

from datetime import *

dt1 = datetime(2010, 1, 1, 10, 20, 30)
dt2 = datetime(2011, 1, 1, 10, 20, 30)

print(dt2 - dt1)
# Output : datetime.timedelta(days=365)

td = dt2 - dt1
print(td)
# Output : datetime.timedelta(days=365)

print(td)
# Output : 365 days, 0:00:00

print(dir(td))
# Output : ['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 'days', 'max', 'microseconds', 'min', 'resolution', 'seconds', 'total_seconds']

print(divmod(td.days, 30))
# Output : (12, 5)

print(divmod(td.days, 7))
# Output : (52, 1)

td1 = timedelta(30)
dt3 = datetime.now()
print(dt3)
# Output : datetime.datetime(2024, 11, 9, 22, 14, 10, 883704)

print(dt3 + td1)
# Output : datetime.datetime(2024, 12, 9, 22, 14, 10, 883704)

print(dt3 + td)
# Output : datetime.datetime(2025, 11, 9, 22, 14, 10, 883704)