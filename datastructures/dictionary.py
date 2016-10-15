#dictionary is like an address-book. we associate KEYS with VALUES
#the KEY must be unique. use only immutable objects for the KEYS of dictionary
#dict class - help(dict)
ab = {
      'Larry' : 'larry@wall.org',
      'Matsumoto' : 'matz@ruby-lang.org',
      'Spammer' : 'spammer@hotmail.com'
     }

print(ab)

#get value for a specified key
ab['Larry']

#length of dictionary
len(ab)

#deleting a key value pair
del ab['Spammer']

#adding a key value pair
ab['Guido'] = 'guido@python.org'

#iterate through all us
# ing items method
for name, address in ab.items():
    print('Contact {0} at {1}'.format(name, address))

#check if something exists
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])
