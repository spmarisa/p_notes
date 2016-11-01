# you can open and use files for reading or writing
# the ability to read or write depends on the mode you have specified for the file opening

poem = '''programming is fun
          programming in python is fun
          never touch that ai thing'''

#open - file name and mode for which it is opened
f = open('poem.txt', 'w')
f.write(poem)
f.close()

f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end=" ")
f.close()

#the mode can be read mode('r'), write mode('w'), append mode('a')
#help(open)

#read can also take an argument that indicates how many characters to read
f = open("poem.txt", "r")
print(f.read(5))

