# python program to use the os Module's builtin functions

import os

print(os.name)
# Output : 'nt'
print(os.getlogin())
# Output : 'Sridharan'



print(os.getcwd())
# Output : 'C:\\Users\\Sridharan'

os.chdir('..')
os.chdir('..')
print(os.getcwd())
# Output : 'C:\\'

print('C:\\Users\\Sridharan')
# Output : C:\Users\Sridharan

os.chdir('D:\\studies')
print(os.getcwd())
# Output : 'D:\\studies'

print(os.listdir())
# Output : ['add - html, css, js', 'c,c++ - DSA', 'college-,dsa using c', 'Data Structures - 12.10.2023 and 13.10.2023 Training', 'debugger', 'fsd-lab', 'git-commands', 'googlesheetsapi-tutorial', 'huggingface-ai.txt', 'java-1day-training', 'javascript-input', 'matrix-website-downloader', 'mernstacktrainingprojects', 'mini-projects', 'OOPS-java', 'projects', 'python-apis', 'python-practice', 'pythonprograms', 'pythonprojcollege', 'React-sample-app-tech-with-tim', 'sanjaysirgithub', 'software engineering']



os.mkdir('For Fun')
print(os.path.isdir('.\\For Fun'))
# Output : True

os.makedirs('GrandParent\\Parent\\Child')
print(os.path.isdir('GrandParent'))
# Output : True

print(os.path.isfile('fun.txt'))
# Output : True



print(os.remove('fun.txt'))
print(os.path.isfile('fun.txt'))
# Output : False

os.rmdir('For Fun')
print(os.path.exists('For Fun'))
# Output : False

os.removedirs('Grandparent\\Parent\\Child')
print(os.path.exists('GrandParent'))
# Output : False



print(os.mkdir('Fun'))
print(os.rename('Fun', 'Boring'))
print(os.rename('fun.txt', 'Boring.py'))