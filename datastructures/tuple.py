# Tuples are used to hold together multiple objects. they are immutable like strings

zoo = ('tiger', 'lion', 'wolf', 'bear')

# lenght of zoo
len(zoo)

# refer by index value
zoo[1]

# create a new tuples
new_zoo = ('rhino', 'ox', zoo)
print(new_zoo)

# refer by index value
new_zoo[1]
new_zoo[2][1]

# lenght of inner tuple
len(new_zoo[2])

# tuple with 0 or 1 item
myempty = ()
single = (1,)
print(single)

# workaround for tuple
a = (1, 2, 3, 4, 5)
a = (1,) + a

# use case - when a matrix has many number of zeros -then use a tuple
matrix = [ [0,0,0,1,0],
           [0,0,0,0,0],
           [0,2,0,0,0],
           [0,0,0,0,0],
           [0,0,0,3,0] ]

matrix = {(0,3): 1, (2, 1): 2, (4, 3): 3}

matrix[0,3]

matrix.get((0,3), 0) # first is key, second is value. get should return if the key if the key is not found in dictionary

