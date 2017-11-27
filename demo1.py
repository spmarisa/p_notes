def length_between(a, b):
    steps = 0

    if a == b:
        return steps

    while a != b:
        if a[0] != b[0]:
            if a[0] > b[0]:
                a[0] = b[0] - 1
                a[1] = b[1] - 1
                steps += 1
            elif a[0] < b[0]:
                a[0] = b[0] + 1
                a[1] = a[1] + 1
                steps += 1
        elif a[1] != b[1]:
            if a[1] > b[1]:
                a[1] = b[1] - 1
                
                steps += 1
            elif a[1] < b[1]:
                a[1] = a[1] + 1
                steps += 1

         return steps

class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        input = []
        steps = 0

        for i in X:
            input.append([X[i], Y[i]])

        if len(input) == 1:
            return 0

        for i in range(len(input) - 1):
            steps += length_between(input(i), input(i+1))

        return steps
