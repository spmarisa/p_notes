import random

#returns a in range of 0.0 - 1.0
random.random()

#random number 0.0 - 10.0
random.uniform(1, 10)

# even integer from 0 to 100
random.randrange(0, 101, 2)
#random integer from o to 9
random.randrange(10)

#random single element
random.choice('abcdefghij')


items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)

random.sample([1, 2, 3, 4, 5],  3)   # Three samples without replacement
