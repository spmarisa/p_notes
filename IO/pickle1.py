# store any python object in a file and then get it back later. this is called storing the object persistently

import pickle

shoplistfile =  'shoplist.data'

shoplist = ['banana', 'papaya', 'mango', 'carrot']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)


