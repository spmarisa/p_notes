#
# import sys
#
#
# n,m = input().strip().split(' ')
# n,m = [int(n),int(m)]
# a = [int(a_temp) for a_temp in input().strip().split(' ')]
# b = [int(b_temp) for b_temp in input().strip().split(' ')]

a = [1, 2]
b = [8, 9, 10, 11, 12]

counter = 0
for i in range(a[len(a) - 1], b[0] + 1):
    print(i)
    if((i % a[len(a) - 1] == 0) & (b[0] % i == 0)):
        counter += 1
print(counter)