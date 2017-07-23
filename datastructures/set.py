# sets are unordered collection of simple objects. these are used when existence of an object in a collection is more
# important than the order or how many times it occur

# create a set
asia = set(['india', 'china', 'japan', 'russia'])

# check if an object is present in a set
'india' in asia
'usa' in asia

# copy one set to another
alagasia = asia.copy()

# add objects to a set
alagasia.add('spain')
alagasia.add('france')

# to remove an object
alagasia.remove('france')

# to check if one is uperset of another
alagasia.issuperset(asia)

# union of two sets
asia | alagasia
asia.union(alagasia)

# intersection of two sets
asia & alagasia
asia.intersection(alagasia)