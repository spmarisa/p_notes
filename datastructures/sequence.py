# lists, tuples and strings are example of sequences.
# indexing operations - which allow us to fetch a particular item in the sequence directly
# lists, tuples and strings have slicing operations

# the start position is included but the end position in exculded from the sequence slice

shoplist = ['apple', 'mango', 'carrot', 'banana']

# value from start to end
shoplist[:]

# values from 1 to 3
shoplist[1:3]

# values from 2 to end
shoplist[2:]

# values from 1 to -1
shoplist[1:-1]

# value from start to end with step size is 1
shoplist[::1]

# values from start to end with step size is 2
shoplist[::2]

# values from start to end with step size -1 -> in reverse
shoplist[::-1]