''' 26.Write a program to perform file and directory 
operations using os and sys modules. '''

import os
import sys

print(sys.version)

os.makedirs('het')
print('Directory Created')

checkdir = os.path.dirname('D:\\het-4076\\python\\20.py')
print('Directory name:',checkdir)

check = os.path.isfile('D:\\het-4076\\python\\20.py')
print('File found in the folder or not:',check)

os.rename('20.py','PRO20.py')
os.remove('ex.py')

bname = os.path.basename('D:\\het-4076\\python\\20.py')
print('File path Basename:',bname)

absolute = os.path.isabs('D:\\het-4076\\python\\20.py')
print('File path Absolute or not:',absolute)



