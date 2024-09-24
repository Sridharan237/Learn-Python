# python program to generate telegram morse code for a given word

codes  = ['._' , '_…' , '_._.' , '_..' , '.' , '.._.' , '__.' , '….' , '..' , '.___']   # morse codes for characters from a to j -> total 10 characters

morse_code = ''

word = 'deface'

for s in word.lower():
    morse_code += codes[ord(s) - 97] + ' '    # ord(s) - 97 -> subtract the ascii value of a from the character in s and add a space to it4

print('Morse Code =>', morse_code.rstrip())
