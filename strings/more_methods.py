name = 'luke skywalker'

name.startswith('luk')

's' in name

#search for given string. return the starting position if present else return -1
name.find('sky')


#to get the index of a given value in a string

fruit = "banana"
fruit.find("n")

#you can pass another parameter as stRTING POSITION
fruit.find("n", 3)

#or you can even pass a range
fruit.find("n", 3, 6)

#join a list by a string
delimeter = '_*_'
list = ['list', 'tuple', 'dictionary', 'set']
delimeter.join(list)


#split a string
a = "ba ba ba, ba banana na"

a.split() #splits based on white space
a.split('a') #split based on the given param

#string comparision they follow dictionary order, first one that occurs is lowest

a = "bacd"
b ="bace"

a < b


