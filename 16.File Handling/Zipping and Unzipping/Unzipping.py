# python program to implement unzipping (decompressing) a zip file into many files in python

from zipfile import *

f = ZipFile('images.zip', 'r')

f.extractall()

f.close()