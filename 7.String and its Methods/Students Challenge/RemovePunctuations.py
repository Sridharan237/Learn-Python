# python program to remove punctuations from a given string

string = input('Enter a string : ')

punctuation = '''\\!()-[]{};:'",<>./?@#$%^&*_~'''
result = ''     # result - String without punctuation

for s in string:
    if s not in punctuation:
        result += s

print('String without punctuation :', result)