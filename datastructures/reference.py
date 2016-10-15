#when creating an object and assign it to a variable, the variable only refers to the object and doesnot represent the
#object itself. only binding the name to the object
list1 = ['java', 'python', 'ruby', 'scala', 'elixir']
list2 = list1

print(list1)
print(list2)

del list1[0]

print(list1)
print(list2)

#copy by making a full slice
list3 = list1[:]

del list1[1]

print(list1)
print(list2)
print(list3)