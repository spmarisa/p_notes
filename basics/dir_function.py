import sys

dir(sys)

#it returns the list of attributes for the current module, list of imported modules is also part of this list
dir()

print(dir(sys))

a = 5

dir()

del a

#it also works on any object
dir('print')
dir(print)