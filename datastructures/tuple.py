#Tuples are used to hold together multiple objects. they are immutable like strings

zoo = ('tiger', 'lion', 'wolf', 'bear')

#lenght of zoo
len(zoo)

#refer by index value
zoo[1]

#create a new tuples
new_zoo = ('rhino', 'ox', zoo)
print(new_zoo)

#refer by index value
new_zoo[1]
new_zoo[2][1]

#lenght of inner tuple
len(new_zoo[2])

#tuple with 0 or 1 item
myempty = ()
single = (1,)
print(single)