# keyword - def, identifier - name of the function
def sayHello():
    print('Hello World!')

sayHello()

#global statement
x = 50
def func():
    global x
    print('x is', x)
    x = 2
    print('changed global x to', x)

func()
print('value of x is', x)



# to make some parameters optional
# you cannot have a parameter with a default argument value preceding a parameter without a default argument value
# in the function’s parameter list.
# only those parameters at the end can be default arguments
def say(message, times = 1):
    print(message * times)

say('Hello')
say('World', 5)



# keyword arguments
# if you have a function with many params and you want to specify only some of them
# then you can give values for such params by naming them
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)



# VarArgs parameters
# to define a function that can take any number of parameters
# When we declare a starred parameter such as *param, then all the positional arguments from that point till the end
# are collected as a tuple called ‘param’. Similarly, when we declare a double-starred parameter such as **param,
# then all the keyword arguments from that point till the end are collected as a dictionary called ‘param’.
def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count
print(total(10, 1, 2, 3, vegetables=50, fruits=100))




# Keyword-only parameters
# If we want to specify certain keyword parameters to be available as keyword-only
# and not as positional arguments, they can be declared after a starred parameter
def total(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)
total(10, 1, 2, 3, extra_number=50)
# raises a error as we have not supplied default argument value
total(10, 1, 2, 3)




# return statement
def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y
print(maximum(2, 3))


