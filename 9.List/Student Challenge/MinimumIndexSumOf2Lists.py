# python program to find the minimum index sum of 2 lists

fav1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']   # Favorite items of person1 - lower the index high the priority
fav2 = ['burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']   # Favorite items of person2 - lower the index high the priority

index1 = len(fav1)
index2 = len(fav2)

for i in range(len(fav1)):
    indx = fav2.index(fav1[i])

    if i + indx < index1 + index2:
        index1 = i
        index2 = indx

print('Minimum Index Sum :', index1+index2)
print('Item (Favorite Item of Both) :', fav1[index1])

