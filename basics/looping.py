n = 0
while n < 5:
    print(n)
    n = n + 1
print("end of input")

i = 0
while i < 10:
    print(i)
    i = i + 1
else:
    print("end of input") #else is optional


for i in range(5):
    print(i)
print("end of input")

for i in range(7, 10): #upto 10 but not 10. i.e, till 9
    print(i)
else:
    print("end of input") #else is optional

for i in range(7, 20, 3):
    print(i)


mysum = 0
for i in range(5, 50):
    mysum += i
    if(mysum > 100):
        break
print("mysum =",mysum)


sw = "abcdefghijklnopqrstuvwxyz"
for index, letter in enumerate(sw):
    print(index)
    print(letter)


#break statement - used to break out of a loop statement
#if you break out of a for or while loop, any corresponding loop else block i snot executed
while True:
    s = input('Enter something : ')
    if s == 'quit':
     break
     print('Length of the string is', len(s))
else:
    print('Done')

#continue statement - to skip the rest of the statements in the current loop, to continue to the next iteration
while True:
    s = input('enter something:')
    if s == 'quit':
        break
    if len(s) < 3:
        print('too small')
        continue
    print('input is of sufficient length')