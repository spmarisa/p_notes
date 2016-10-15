x = 50

def func():
    global x

    print('value of x is', x)

    x = 2
    print('now value of x is', x)
func()
print('value of x is', x)
