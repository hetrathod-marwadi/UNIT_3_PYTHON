''' 27.Write a program to copy move and delete files 
using shutil module.'''

import shutil
import os

if os.path.isfile('1.py'):
    if not os.path.isdir('pydir'):
        os.makedirs('pydir')
    shutil.copy('1.py','pydir')
    if not os.path.isdir('het'):
        os.makedirs('het')
    shutil.move('D:\\het-4076\\python\\pydir\\1.py','het')
    print("File moved successfully.")

    os.remove('het\\1.py')
    print("File deleted successfully.")
