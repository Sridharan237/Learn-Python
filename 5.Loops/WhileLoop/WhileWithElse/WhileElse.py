# python program to implement while with else without break and with break statement

# while with else - without break
count = 1

while count <= 10:
    print(count)
    count += 1
else:
    print('Printed all 10 numbers')

print('End of the program')

# while with else - with break
count = 1

while count <= 10:
    print(count)
    count += 1

    if count > 5:
        break

else:
    print('Printed all 10 numbers')

print('End of the program')