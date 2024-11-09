# python program to implement time module and datetime module (datetime class)

import time
import datetime

# time module (struct_time class)

print(time.time())
# Output : 1731154213.6480482

lt = time.localtime()
print(lt)
# Output : time.struct_time(tm_year=2024, tm_mon=11, tm_mday=9, tm_hour=17, tm_min=43, tm_sec=15, tm_wday=5, tm_yday=314, tm_isdst=0)
print(type(lt))
# Output : <class 'time.struct_time'>
print(lt.tm_year)
# Output : 2024
print(lt.tm_mon)
# Output : 11
print(lt.tm_mday)
# Output : 9
print(lt.tm_hour)
# Output : 17
print(lt.tm_min)
# Output : 43
print(lt.tm_sec)
# Output : 15
print(lt.tm_wday)
# Output : 5
print(lt.tm_yday)
# Output : 314
print(lt.tm_isdst)
# Output : 0
lt = time.localtime(time.time()/2)
print(lt)
# Output : time.struct_time(tm_year=1997, tm_mon=6, tm_mday=6, tm_hour=11, tm_min=37, tm_sec=52, tm_wday=4, tm_yday=157, tm_isdst=0)
print(lt.tm_year)
# Output : 1997
print(lt.tm_mon)
# Output : 6
print(lt.tm_mday)
# Output : 6

ct = time.ctime()
print(ct)
# Output : Sat Nov  9 17:46:54 2024



# datetime module (datetime class)

dt = datetime.datetime.now()
print(dt)
# Output : 2024-11-09 17:47:29.082292
print(type(dt))
# Output : <class 'datetime.datetime'>

dt = datetime.datetime.today()
print(dt)
# Output : 2024-11-09 17:48:17.957545
print(type(dt))
# Output : <class 'datetime.datetime'>
print(dt)
# Output : datetime.datetime(2024, 11, 9, 17, 48, 17, 957545)