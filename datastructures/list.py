# list holds an ordered collection of items
# once created a list, you can add, remove or search for items in the list
# list is a mutable data type

shoplist = ['apple', 'mango', 'carrot', 'banana']

# print the list
print(shoplist)

# length of list
len(shoplist)

# create a list
list(range(11, 17))

list(range(6))

list(range(0, 16, 5))

# list can consist of multiple types

a = ['string', 'a', 2, 5.6]

# iterate through each in list
# use of the end keyword argument, that we want to end the output with a space instead of the usual line break.
print('These items are:', end='')
for item in shoplist:
    print(item, end=' ')

# add a new value to list in the end
shoplist.append('rice')

# sort the list
shoplist.sort()

# refer by index value
shoplist[0]

# delete the value
del shoplist[0]

# to find a given in the list
a = ['a', 'b', 'c', 'd', 'e']

'a' in a


# add 2 lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b


# we can slice a list too just like a string
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[2:5])

# replace a portion of a string
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[0:6] = [0 , 0]


# cloning list, if you assign one to other they refer to te same object
a = [45, 678, 243]
b = a
b = a[:]

# nested lists, lists with a list or for matrices

list = [[1,2,3], [4,5,6], [9,0,1]]

# split a string
a = "ba ba ba, ba banana na"

a.split() #splits based on white space
a.split('a') #split based on the given param

# join a list by a string
delimeter = '_*_'
list = ['list', 'tuple', 'dictionary', 'set']
delimeter.join(list)

