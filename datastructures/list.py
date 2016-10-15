#list holds an ordered collection of items
#once created a list, you can add, remove or search for items in the list
#list is a mutable data type

shoplist = ['apple', 'mango', 'carrot', 'banana']

#print the list
print(shoplist)

# lenght of list
len(shoplist)

#iterate through each in list
# use of the end keyword argument, that we want to end the output with a space instead of the usual line break.
print('These items are:', end='')
for item in shoplist:
    print(item, end=' ')

# add a new value to list in the end
shoplist.append('rice')

#sort the list
shoplist.sort()

#refer by index value
shoplist[0]

#delete the value
del shoplist[0]

