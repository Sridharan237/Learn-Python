# python program to implement infinite loop, jump statements in python like break, continue, pass

# 1. Infinite Loop - with True in Condition
# while True:
#     print('Hello')

# 2. Infinite Loop - without modifying loop control variable
# count = 0
# while count < 10:
#     print('hello')

# Infinite Loop - Positive or Negative or Zero
# while True:
#     n = int(input('Enter a number : '))
#
#     if n > 0:
#         print('Positive Number')
#     elif n < 0:
#         print('Negative Number')
#     else:
#         print('Zero')

# Jump Statements - break, continue, pass
# 1. break - positive or negative or zero -> only when n is zero the loop will be broken
# while True:
#     n = int(input('Enter a number : '))
#
#     if n > 0:
#         print('Positive Number')
#     elif n < 0:
#         print('Negative Number')
#     else:
#         print('Zero')
#         break

# 2. continue - print given input number when it is not divisible by 3 and if a number is divisible by 3 don't print it and print 10 numbers using counter variable and continue statement
# count = 0
# while count < 10:
#     n = int(input('Enter a number : '))
#
#     if n % 3 == 0:
#         continue
#
#     count += 1
#     print(n)

# # 3. pass - print given input number when it is not divisible by 3 and if a number is divisible by 3 don't print it and print 10 numbers using counter variable and pass statement
count = 0
while count < 10:
    n = int(input('Enter a number : '))

    if n % 3 == 0:
        pass
    else:
        print(n)
    count += 1




