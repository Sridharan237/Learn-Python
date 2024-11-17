# python program to use the os.path submodule

import os
import time

print(os.path.exists('D:\\studies\\huggingface-ai.txt'))
# Output : True

print(os.path.exists('D:\\studies\\Hello'))
# Output : False

print(os.path.isfile('D:\\studies\\huggingface-ai.txt'))
# Output : True

print(os.path.isfile('D:\\studies\\Hello'))
# Output : False

print(os.path.isdir('D:\\studies\\Hello'))
# Output : False

print(os.path.isdir('D:\\studies\\huggingface-ai.txt'))
# Output : False

print(os.path.isdir('D:\\studies\\'))
# Output : True



print(os.path.split('D:\\studies\\huggingface-ai.txt'))
# Output : ('D:\\studies', 'huggingface-ai.txt')

print(os.path.join('D:\\studies', 'huggingface-ai.txt'))
# Output : 'D:\\studies\\huggingface-ai.txt'



print(os.path.basename('D:\\studies\\huggingface-ai.txt'))
# Output : 'huggingface-ai.txt'

print(os.path.dirname('D:\\studies\\huggingface-ai.txt'))
# Output : 'D:\\studies'



print(os.path.getmtime('D:\\studies\\huggingface-ai.txt'))
# Output : 1723444042.446967

print(time.ctime(os.path.getmtime('D:\\studies\\huggingface-ai.txt')))
# Output : 'Mon Aug 12 11:57:22 2024'

print(os.path.getatime('D:\\studies\\huggingface-ai.txt'))
# Output : 1723444042.446967

print(time.ctime(os.path.getatime('D:\\studies\\huggingface-ai.txt')))
# Output : 'Mon Aug 12 11:57:22 2024'

print(time.ctime(os.path.getctime('D:\\studies\\huggingface-ai.txt')))
# Output : 'Mon Aug 12 11:57:22 2024'

print(os.path.getctime('D:\\studies\\huggingface-ai.txt'))
# Output : 1723444042.4439652

print(time.ctime(os.path.getatime('D:\\studies\\huggingface-ai.txt')))
# Output : 'Mon Aug 12 11:57:22 2024'

print(time.ctime(os.path.getatime('D:\\studies\\huggingface-ai.txt')))
# Output : 'Mon Aug 12 11:57:22 2024'

print(time.ctime(os.path.getatime('D:\\studies\\huggingface-ai.txt')))
# Output : 'Mon Aug 12 11:57:22 2024'

print(time.ctime(os.path.getatime('D:\\studies\\huggingface-ai.txt')))
# Output : 'Mon Aug 12 11:57:22 2024'



'''print(os.chdir('C:\MinGW\bin'))
# Output : <stdin>:1: SyntaxWarning: invalid escape sequence '\M'

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect: 'C:\\MinGW\x08in' '''

print(os.chdir('C:\\MinGW\\bin'))
# Output :

print(os.getcwd())
# Output : 'C:\\MinGW\\bin'



print(os.path.relpath('C:\\MinGW\\lib\\libuuid.a'))
# Output : '..\\lib\\libuuid.a'

print(os.path.abspath('..\\lib\\libuuid.a'))
# Output : 'C:\\MinGW\\lib\\libuuid.a'