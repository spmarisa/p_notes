#if you wanted to reuse a number of functions in other programs that you write
# for writing modules, but the simplest way is to create a file with a .py extension that contains functions and variables.
# another way is to write modules in native language(like c, python interpreter is written in c)
#a module can be imported by another program to make use of its functionality

import sys
print('the command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')

import os
print(os.getcwd())


from math import sqrt
print("Square root of 16 is", sqrt(16))

#every module has a name
#statements in a module can find out the name of their module
#This is handy for the particular purpose of figuring out whether the module is being run standalone or being imported
#to import this - import file_name
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('IO am being imported from another module')
