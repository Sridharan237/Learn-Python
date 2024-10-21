# python program to zip(compress) - some set of files in python

from zipfile import *

f = ZipFile('images.zip', 'w', ZIP_DEFLATED)

f.write('Python-logo.jpg')
f.write('Java-logo.jpg')
f.write('C-logo.jpg')
f.write('CPP-logo.jpg')
f.write('Csharp-logo.jpg')

f.close()