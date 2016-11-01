
def printFibbo(n):
    if(n <= 1):
        return n
    else:
        return printFibbo(n-1) + printFibbo(n-2)


print(printFibbo(30))

previous = {0:1, 1:1}
def fibonacci(n):
    if n in previous:
        return previous[n]
    else:
        newValue = fibonacci(n-1) + fibonacci(n-2)
        previous[n] = newValue
    return newValue

fibonacci(10)
print(previous)