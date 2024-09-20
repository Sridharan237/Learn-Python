# python program to implement C style formatting (or) printing in python

rollno = 10
name = 'Ravi'
avg = 86.29714

print('Student name is %s, His rollno is %d and average is %f' % (name, rollno, avg))
# Output : Student name is Ravi, His rollno is 10 and average is 86.297140

print('Student name is %s' % name)
# Output : Student name is Ravi

print('Student name is %10s' % name)        # Right Align -> name - width 10 
# Output : Student name is       Ravi

print('Student name is %-10s' % name)       # Left Align -> name - width 10
# Output : Student name is Ravi

print('rollno is %8d' % rollno)
# Output : rollno is       10

print('rollno is %-8d' % rollno)
# Output : rollno is 10

print('rollno is %-8d and' % rollno)
# Output : rollno is 10       and

print('average is %f' % avg)
# Output : average is 86.297140

print('average is %2.3f' % avg)
# Output : average is 86.297

print('average is %1.3f' % avg)
# Output : average is 86.297

print('average is %0.3f' % avg)
# Output : average is 86.297

print('average is %.3f' % avg)
# Output : average is 86.297