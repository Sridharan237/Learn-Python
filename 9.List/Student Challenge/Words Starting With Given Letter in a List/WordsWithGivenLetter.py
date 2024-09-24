# python program to find the words starting with a given letter in a list

food = ['pizza', 'burger', 'nuggets', 'pasta', 'noodles', 'parotta']

letter = input('Enter a small case alphabet : ')    # letter - small case alphabet character

print('Words Starting With Given Letter are :')

flag = 0

for item in food:
    if item.startswith(letter):
        print(item)
        flag = 1
else:
    if flag == 0:
        print('No Words Starting With Given Letter Found')