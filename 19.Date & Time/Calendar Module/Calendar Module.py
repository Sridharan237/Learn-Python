# python program to use the classes available in calendar module - classes (Calendar, TextCalendar, HTMLCalendar)

from calendar import *



# Calendar class

print(firstweekday())
# Output : 0

print(isleap(2024))
# Output : True

print(isleap(2021))
# Output : False

print(leapdays(2000, 2024))
# Output : 6

print(prmonth(2024, 11))
'''Output : 
    November 2024
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30'''

print(prmonth(2024, 12))
'''Output :
    December 2024
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31'''

c = Calendar()
print(c)
# Output : <calendar.Calendar object at 0x000001C964CE66C0>

for i in c.iterweekdays():
    print(i)
'''Output : 
0
1
2
3
4
5
6'''

for i in c.itermonthdates(2024, 11):
    print(i)
'''Output : 
2024-10-28
2024-10-29
2024-10-30
2024-10-31
2024-11-01
2024-11-02
2024-11-03
2024-11-04
2024-11-05
2024-11-06
2024-11-07
2024-11-08
2024-11-09
2024-11-10
2024-11-11
2024-11-12
2024-11-13
2024-11-14
2024-11-15
2024-11-16
2024-11-17
2024-11-18
2024-11-19
2024-11-20
2024-11-21
2024-11-22
2024-11-23
2024-11-24
2024-11-25
2024-11-26
2024-11-27
2024-11-28
2024-11-29
2024-11-30
2024-12-01'''

for i in c.monthdatescalendar(2024, 11):
    print(i)
'''Output : 
[datetime.date(2024, 10, 28), datetime.date(2024, 10, 29), datetime.date(2024, 10, 30), datetime.date(2024, 10, 31), datetime.date(2024, 11, 1), datetime.date(2024, 11, 2), datetime.date(2024, 11, 3)]
[datetime.date(2024, 11, 4), datetime.date(2024, 11, 5), datetime.date(2024, 11, 6), datetime.date(2024, 11, 7), datetime.date(2024, 11, 8), datetime.date(2024, 11, 9), datetime.date(2024, 11, 10)]
[datetime.date(2024, 11, 11), datetime.date(2024, 11, 12), datetime.date(2024, 11, 13), datetime.date(2024, 11, 14), datetime.date(2024, 11, 15), datetime.date(2024, 11, 16), datetime.date(2024, 11, 17)]
[datetime.date(2024, 11, 18), datetime.date(2024, 11, 19), datetime.date(2024, 11, 20), datetime.date(2024, 11, 21), datetime.date(2024, 11, 22), datetime.date(2024, 11, 23), datetime.date(2024, 11, 24)]
[datetime.date(2024, 11, 25), datetime.date(2024, 11, 26), datetime.date(2024, 11, 27), datetime.date(2024, 11, 28), datetime.date(2024, 11, 29), datetime.date(2024, 11, 30), datetime.date(2024, 12, 1)]'''



# TextCalendar - class

c = TextCalendar()

print(print(c))
# Output : <calendar.TextCalendar object at 0x000001C964E5BEF0>

print(c.prmonth(2024, 11))
'''Output :
    November 2024
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30'''

print(c.formatmonth(2024, 11, 10, 5))
'''Output :
    '                               November 2024\n\n\n\n\n  Monday    Tuesday   Wednesday   Thursday    Friday    Saturday    Sunday\n\n\n\n\n                                                 1          2          3\n\n\n\n\n     4          5          6          7          8          9         10\n\n\n\n\n    11         12         13         14         15         16         17\n\n\n\n\n    18         19         20         21         22         23         24\n\n\n\n\n    25         26         27         28         29         30\n\n\n\n\n' '''

print(c.pryear(2024))
'''Output :
                                             2024

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                   1  2  3
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       4  5  6  7  8  9 10
15 16 17 18 19 20 21      12 13 14 15 16 17 18      11 12 13 14 15 16 17
22 23 24 25 26 27 28      19 20 21 22 23 24 25      18 19 20 21 22 23 24
29 30 31                  26 27 28 29               25 26 27 28 29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7             1  2  3  4  5                      1  2
 8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9
15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16
22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23
29 30                     27 28 29 30 31            24 25 26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                         1
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8
15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15
22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22
29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29
                                                    30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3                         1
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       2  3  4  5  6  7  8
14 15 16 17 18 19 20      11 12 13 14 15 16 17       9 10 11 12 13 14 15
21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
                                                    30 31'''
                                                    
print(c.formatyear(2024, 5, 5))
'''Output : '                                                                  2024\n\n\n\n\n\n\n\n\n\n                 January
                     February                                        March\n\n\n\n\n Mon   Tue   Wed   Thu   Fri   Sat   Sun        Mon   Tue   Wed   Thu   Fri   Sat   Sun        Mon   Tue   Wed   Thu   Fri   Sat   Sun\n\n\n\n\n   1     2     3     4     5     6     7                            1     2     3     4                                  1     2     3\n\n\n\n\n   8     9    10    11    12    13    14          5     6     7     8     9    10    11          4     5     6     7     8     9    10\n\n\n\n\n  15    16    17    18    19    20    21         12    13    14    15    16    17    18         11    12    13    14    15    16    17\n\n\n\n\n  22    23    24    25    26    27    28         19    20    21    22    23    24    25         18    19    20    21    22    23    24\n\n\n\n\n  29    30    31                                 26    27    28    29                           25    26    27    28    29    30    31\n\n\n\n\n\n\n\n\n\n                  April                                           May                                            June\n\n\n\n\n Mon   Tue   Wed   Thu   Fri   Sat   Sun        Mon   Tue   Wed   Thu   Fri   Sat   Sun        Mon   Tue   Wed   Thu   Fri   Sat   Sun\n\n\n\n\n   1     2     3     4     5     6     7                      1     2     3     4     5
                1     2\n\n\n\n\n   8     9    10    11    12    13    14          6     7     8     9    10    11    12          3     4     5     6     7     8     9\n\n\n\n\n  15    16    17    18    19    20    21         13    14    15    16    17    18    19         10    11    12    13    14    15    16\n\n\n\n\n  22    23    24    25    26    27    28         20    21    22    23    24    25    26         17    18    19    20    21    22    23\n\n\n\n\n  29    30                                       27    28    29    30    31                     24    25    26    27    28    29    30\n\n\n\n\n\n\n\n\n\n                   July
              August                                       September\n\n\n\n\n Mon   Tue   Wed   Thu   Fri   Sat   Sun        Mon   Tue   Wed   Thu   Fri   Sat   Sun        Mon   Tue   Wed   Thu   Fri   Sat   Sun\n\n\n\n\n   1     2     3     4     5     6     7                            1     2     3     4                                              1\n\n\n\n\n   8     9    10    11    12    13    14          5     6     7     8     9    10    11          2     3     4     5     6     7     8\n\n\n\n\n  15    16    17    18    19    20    21         12    13    14    15    16    17    18          9    10    11    12    13    14    15\n\n\n\n\n  22    23    24    25    26    27    28         19    20    21    22    23    24    25         16    17    18    19    20    21    22\n\n\n\n\n  29    30    31                                 26    27    28    29    30    31               23    24    25    26    27    28    29\n\n\n\n\n                                                                                                30\n\n\n\n\n\n\n\n\n\n
     October                                        November                                       December\n\n\n\n\n Mon   Tue   Wed   Thu   Fri   Sat   Sun        Mon   Tue   Wed   Thu   Fri   Sat   Sun        Mon   Tue   Wed   Thu   Fri   Sat   Sun\n\n\n\n\n         1     2     3     4     5     6                                  1     2     3                                              1\n\n\n\n\n   7     8     9    10    11    12    13          4     5     6     7     8     9    10          2     3     4     5     6     7     8\n\n\n\n\n  14    15    16    17    18    19    20         11    12    13    14    15    16    17          9    10    11    12    13    14    15\n\n\n\n\n  21    22    23    24    25    26    27         18    19    20    21    22    23    24         16    17    18    19    20    21    22\n\n\n\n\n  28    29    30    31                           25    26    27    28    29    30               23    24    25    26    27    28    29\n\n\n\n\n
     30    31\n\n\n\n\n' '''


# HTMLCalendar - class

c = HTMLCalendar()

print(c)
# Output : <calendar.HTMLCalendar object at 0x000001C964E5BE00>

print(c.formatmonth(2024, 11))
# Output : '<table border="0" cellpadding="0" cellspacing="0" class="month">\n<tr><th colspan="7" class="month">November 2024</th></tr>\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>\n<tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="fri">1</td><td class="sat">2</td><td class="sun">3</td></tr>\n<tr><td class="mon">4</td><td class="tue">5</td><td class="wed">6</td><td class="thu">7</td><td class="fri">8</td><td class="sat">9</td><td class="sun">10</td></tr>\n<tr><td class="mon">11</td><td class="tue">12</td><td class="wed">13</td><td class="thu">14</td><td class="fri">15</td><td class="sat">16</td><td class="sun">17</td></tr>\n<tr><td class="mon">18</td><td class="tue">19</td><td class="wed">20</td><td class="thu">21</td><td class="fri">22</td><td class="sat">23</td><td class="sun">24</td></tr>\n<tr><td class="mon">25</td><td class="tue">26</td><td class="wed">27</td><td class="thu">28</td><td class="fri">29</td><td class="sat">30</td><td class="noday">&nbsp;</td></tr>\n</table>\n'

print(c.formatyear(2024))
# Output : '<table border="0" cellpadding="0" cellspacing="0" class="year">\n<tr><th colspan="3" class="year">2024</th></tr><tr><td><table border="0" cellpadding="0" cellspacing="0" class="month">\n<tr><th colspan="7" class="month">January</th></tr>\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>\n<tr><td class="mon">1</td><td class="tue">2</td><td class="wed">3</td><td class="thu">4</td><td class="fri">5</td><td class="sat">6</td><td class="sun">7</td></tr>\n<tr><td class="mon">8</td><td class="tue">9</td><td class="wed">10</td><td class="thu">11</td><td class="fri">12</td><td class="sat">13</td><td class="sun">14</td></tr>\n<tr><td class="mon">15</td><td class="tue">16</td><td class="wed">17</td><td class="thu">18</td><td class="fri">19</td><td class="sat">20</td><td class="sun">21</td></tr>\n<tr><td class="mon">22</td><td class="tue">23</td><td class="wed">24</td><td class="thu">25</td><td class="fri">26</td><td class="sat">27</td><td class="sun">28</td></tr>\n<tr><td class="mon">29</td><td class="tue">30</td><td class="wed">31</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>\n</table>\n</td><td><table border="0" cellpadding="0" cellspacing="0" class="month">\n<tr><th colspan="7" class="month">February</th></tr>\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>\n<tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="thu">1</td><td class="fri">2</td><td class="sat">3</td><td class="sun">4</td></tr>\n<tr><td class="mon">5</td><td class="tue">6</td><td class="wed">7</td><td class="thu">8</td><td class="fri">9</td><td class="sat">10</td><td class="sun">11</td></tr>\n<tr><td class="mon">12</td><td class="tue">13</td><td class="wed">14</td><td class="thu">15</td><td class="fri">16</td><td class="sat">17</td><td class="sun">18</td></tr>\n<tr><td class="mon">19</td><td class="tue">20</td><td class="wed">21</td><td class="thu">22</td><td class="fri">23</td><td class="sat">24</td><td class="sun">25</td></tr>\n<tr><td class="mon">26</td><td class="tue">27</td><td class="wed">28</td><td class="thu">29</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>\n</table>\n</td><td><table border="0" cellpadding="0" cellspacing="0" class="month">\n<tr><th colspan="7" class="month">March</th></tr>\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>\n<tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="fri">1</td><td class="sat">2</td><td class="sun">3</td></tr>\n<tr><td class="mon">4</td><td class="tue">5</td><td class="wed">6</td><td class="thu">7</td><td class="fri">8</td><td class="sat">9</td><td class="sun">10</td></tr>\n<tr><td class="mon">11</td><td class="tue">12</td><td class="wed">13</td><td class="thu">14</td><td class="fri">15</td><td class="sat">16</td><td class="sun">17</td></tr>\n<tr><td class="mon">18</td><td class="tue">19</td><td class="wed">20</td><td class="thu">21</td><td class="fri">22</td><td class="sat">23</td><td class="sun">24</td></tr>\n<tr><td class="mon">25</td><td class="tue">26</td><td class="wed">27</td><td class="thu">28</td><td class="fri">29</td><td class="sat">30</td><td class="sun">31</td></tr>\n</table>\n</td></tr><tr><td><table border="0" cellpadding="0" cellspacing="0" class="month">\n<tr><th colspan="7" class="month">April</th></tr>\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>\n<tr><td class="mon">1</td><td class="tue">2</td><td class="wed">3</td><td class="thu">4</td><td class="fri">5</td><td class="sat">6</td><td class="sun">7</td></tr>\n<tr><td class="mon">8</td><td class="tue">9</td><td class="wed">10</td><td class="thu">11</td><td class="fri">12</td><td class="sat">13</td><td class="sun">14</td></tr>\n<tr><td class="mon">15</td><td class="tue">16</td><td class="wed">17</td><td class="thu">18</td><td class="fri">19</td><td class="sat">20</td><td class="sun">21</td></tr>\n<tr><td class="mon">22</td><td class="tue">23</td><td class="wed">24</td><td class="thu">25</td><td class="fri">26</td><td class="sat">27</td><td class="sun">28</td></tr>\n<tr><td class="mon">29</td><td class="tue">30</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>\n</table>\n</td><td><table border="0" cellpadding="0" cellspacing="0" class="month">\n<tr><th colspan="7" class="month">May</th></tr>\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>\n<tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="wed">1</td><td class="thu">2</td><td class="fri">3</td><td class="sat">4</td><td class="sun">5</td></tr>\n<tr><td class="mon">6</td><td class="tue">7</td><td class="wed">8</td><td class="thu">9</td><td class="fri">10</td><td class="sat">11</td><td class="sun">12</td></tr>\n<tr><td class="mon">13</td><td class="tue">14</td><td class="wed">15</td><td class="thu">16</td><td class="fri">17</td><td class="sat">18</td><td class="sun">19</td></tr>\n<tr><td class="mon">20</td><td class="tue">21</td><td class="wed">22</td><td class="thu">23</td><td class="fri">24</td><td class="sat">25</td><td class="sun">26</td></tr>\n<tr><td class="mon">27</td><td class="tue">28</td><td class="wed">29</td><td class="thu">30</td><td class="fri">31</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>\n</table>\n</td><td><table border="0" cellpadding="0" cellspacing="0" class="month">\n<tr><th colspan="7" class="month">June</th></tr>\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>\n<tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="sat">1</td><td class="sun">2</td></tr>\n<tr><td class="mon">3</td><td class="tue">4</td><td class="wed">5</td><td class="thu">6</td><td class="fri">7</td><td class="sat">8</td><td class="sun">9</td></tr>\n<tr><td class="mon">10</td><td class="tue">11</td><td class="wed">12</td><td class="thu">13</td><td class="fri">14</td><td class="sat">15</td><td class="sun">16</td></tr>\n<tr><td class="mon">17</td><td class="tue">18</td><td class="wed">19</td><td class="thu">20</td><td class="fri">21</td><td class="sat">22</td><td class="sun">23</td></tr>\n<tr><td class="mon">24</td><td class="tue">25</td><td class="wed">26</td><td class="thu">27</td><td class="fri">28</td><td class="sat">29</td><td class="sun">30</td></tr>\n</table>\n</td></tr><tr><td><table border="0" cellpadding="0" cellspacing="0" class="month">\n<tr><th colspan="7" class="month">July</th></tr>\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>\n<tr><td class="mon">1</td><td class="tue">2</td><td class="wed">3</td><td class="thu">4</td><td class="fri">5</td><td class="sat">6</td><td class="sun">7</td></tr>\n<tr><td class="mon">8</td><td class="tue">9</td><td class="wed">10</td><td class="thu">11</td><td class="fri">12</td><td class="sat">13</td><td class="sun">14</td></tr>\n<tr><td class="mon">15</td><td class="tue">16</td><td class="wed">17</td><td class="thu">18</td><td class="fri">19</td><td class="sat">20</td><td class="sun">21</td></tr>\n<tr><td class="mon">22</td><td class="tue">23</td><td class="wed">24</td><td class="thu">25</td><td class="fri">26</td><td class="sat">27</td><td class="sun">28</td></tr>\n<tr><td class="mon">29</td><td class="tue">30</td><td class="wed">31</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>\n</table>\n</td><td><table border="0" cellpadding="0" cellspacing="0" class="month">\n<tr><th colspan="7" class="month">August</th></tr>\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>\n<tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="thu">1</td><td class="fri">2</td><td class="sat">3</td><td class="sun">4</td></tr>\n<tr><td class="mon">5</td><td class="tue">6</td><td class="wed">7</td><td class="thu">8</td><td class="fri">9</td><td class="sat">10</td><td class="sun">11</td></tr>\n<tr><td class="mon">12</td><td class="tue">13</td><td class="wed">14</td><td class="thu">15</td><td class="fri">16</td><td class="sat">17</td><td class="sun">18</td></tr>\n<tr><td class="mon">19</td><td class="tue">20</td><td class="wed">21</td><td class="thu">22</td><td class="fri">23</td><td class="sat">24</td><td class="sun">25</td></tr>\n<tr><td class="mon">26</td><td class="tue">27</td><td class="wed">28</td><td class="thu">29</td><td class="fri">30</td><td class="sat">31</td><td class="noday">&nbsp;</td></tr>\n</table>\n</td><td><table border="0" cellpadding="0" cellspacing="0" class="month">\n<tr><th colspan="7" class="month">September</th></tr>\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>\n<tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="sun">1</td></tr>\n<tr><td class="mon">2</td><td class="tue">3</td><td class="wed">4</td><td class="thu">5</td><td class="fri">6</td><td class="sat">7</td><td class="sun">8</td></tr>\n<tr><td class="mon">9</td><td class="tue">10</td><td class="wed">11</td><td class="thu">12</td><td class="fri">13</td><td class="sat">14</td><td class="sun">15</td></tr>\n<tr><td class="mon">16</td><td class="tue">17</td><td class="wed">18</td><td class="thu">19</td><td class="fri">20</td><td class="sat">21</td><td class="sun">22</td></tr>\n<tr><td class="mon">23</td><td class="tue">24</td><td class="wed">25</td><td class="thu">26</td><td class="fri">27</td><td class="sat">28</td><td class="sun">29</td></tr>\n<tr><td class="mon">30</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>\n</table>\n</td></tr><tr><td><table border="0" cellpadding="0" cellspacing="0" class="month">\n<tr><th colspan="7" class="month">October</th></tr>\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>\n<tr><td class="noday">&nbsp;</td><td class="tue">1</td><td class="wed">2</td><td class="thu">3</td><td class="fri">4</td><td class="sat">5</td><td class="sun">6</td></tr>\n<tr><td class="mon">7</td><td class="tue">8</td><td class="wed">9</td><td class="thu">10</td><td class="fri">11</td><td class="sat">12</td><td class="sun">13</td></tr>\n<tr><td class="mon">14</td><td class="tue">15</td><td class="wed">16</td><td class="thu">17</td><td class="fri">18</td><td class="sat">19</td><td class="sun">20</td></tr>\n<tr><td class="mon">21</td><td class="tue">22</td><td class="wed">23</td><td class="thu">24</td><td class="fri">25</td><td class="sat">26</td><td class="sun">27</td></tr>\n<tr><td class="mon">28</td><td class="tue">29</td><td class="wed">30</td><td class="thu">31</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>\n</table>\n</td><td><table border="0" cellpadding="0" cellspacing="0" class="month">\n<tr><th colspan="7" class="month">November</th></tr>\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>\n<tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="fri">1</td><td class="sat">2</td><td class="sun">3</td></tr>\n<tr><td class="mon">4</td><td class="tue">5</td><td class="wed">6</td><td class="thu">7</td><td class="fri">8</td><td class="sat">9</td><td class="sun">10</td></tr>\n<tr><td class="mon">11</td><td class="tue">12</td><td class="wed">13</td><td class="thu">14</td><td class="fri">15</td><td class="sat">16</td><td class="sun">17</td></tr>\n<tr><td class="mon">18</td><td class="tue">19</td><td class="wed">20</td><td class="thu">21</td><td class="fri">22</td><td class="sat">23</td><td class="sun">24</td></tr>\n<tr><td class="mon">25</td><td class="tue">26</td><td class="wed">27</td><td class="thu">28</td><td class="fri">29</td><td class="sat">30</td><td class="noday">&nbsp;</td></tr>\n</table>\n</td><td><table border="0" cellpadding="0" cellspacing="0" class="month">\n<tr><th colspan="7" class="month">December</th></tr>\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>\n<tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="sun">1</td></tr>\n<tr><td class="mon">2</td><td class="tue">3</td><td class="wed">4</td><td class="thu">5</td><td class="fri">6</td><td class="sat">7</td><td class="sun">8</td></tr>\n<tr><td class="mon">9</td><td class="tue">10</td><td class="wed">11</td><td class="thu">12</td><td class="fri">13</td><td class="sat">14</td><td class="sun">15</td></tr>\n<tr><td class="mon">16</td><td class="tue">17</td><td class="wed">18</td><td class="thu">19</td><td class="fri">20</td><td class="sat">21</td><td class="sun">22</td></tr>\n<tr><td class="mon">23</td><td class="tue">24</td><td class="wed">25</td><td class="thu">26</td><td class="fri">27</td><td class="sat">28</td><td class="sun">29</td></tr>\n<tr><td class="mon">30</td><td class="tue">31</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>\n</table>\n</td></tr></table>'