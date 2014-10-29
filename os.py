#
import os
import sys
# Return n random bytes suitable for cryptographic use.
print os.urandom(3)

# file
os.mkdir('test',0777)
os.chdir('test')
with open('test.py', mode = 'wb'):
    pass
print os.listdir(os.getcwd())
os.rename('test.py', 'test1.py')
print os.listdir(os.getcwd())

