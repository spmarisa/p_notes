i = 5
#think of it as creating an object i of class int
#a class can have also methods, functions defined for use with the respect to that class only

# oo programming -  combine data and functionality and wrap it inside something called an object.
#CLASSES - creates a new type
#OBJECTS - instances of the class
#fields and methods of the class, collectively reffered to as attributes
#instance variables and class variables

class Intro:
    def sayHello(self):
        print('HELLO WORLD')

i = Intro()
i.sayHello()

# __init__ method is run as soon as an object of a class is instantiated - useful to do any initialization with your object
class Person:
    def __init__(self, name):
        self.name = name

    def sayhello(self):
        print('hello', self.name)

p = Person('stark')
p.sayhello()


# refer to the variables and methods of the same object using the self only

#all methods are public. one exception - if you use data members with names using the double underscore(__private var)
# to make it a private variable