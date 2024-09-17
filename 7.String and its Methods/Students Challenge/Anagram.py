# python program to check whether two strings are anagram or not

s1 = input('Enter first string : ')
s2 = input('Enter second string : ')

if len(s1) != len(s2):
    print('Not Anagram')
else:
    l1 = sorted(s1)
    l2 = sorted(s2)

    for i in range(0, len(l1)):
        if l1[i] != l2[i]:
            print('Not Anagram')
            break
    else:
        print('Anagram')