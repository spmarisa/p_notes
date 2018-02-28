def rotate_matrix(a1):
    n = len(a1)
    number_of_layers = round(len(a1) / 2)

    for layer in range(number_of_layers):
        first = layer
        last = n - 1 - layer

        for i in range(last):
            offset = i - first;
            top = a1[first][i]

            #     left -> top
            a1[first][i] = a1[last-offset][first]
            #      botton -> left
            a1[last-offset][first] = a1[last][last - offset]
            #      right -> bottom
            a1[last][last - offset] = a1[i][last]
            #      top -> right
            a1[i][last] = top

    return a1


a1 = [[1,  2,  3,  4],
     [5,  6,  7,  8],
     [9,  10, 11, 12],
     [13, 14, 15, 16]]

a2 = [[13, 9,  5, 1],
     [14, 10, 6, 2],
     [15, 11, 7, 3],
     [16, 12, 8, 4]]

print(a1)
print(rotate_matrix(a1))
