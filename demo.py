arr = [[-1, -1, 0, -9, -2, -2],
       [-2, -1, -6, -8, -2, -5],
       [-1, -1, -1, 2, 3, 4],
       [-1, -9, -2, -4, -4, -5],
       [-7, -3, -3, -2, -9, -9],
       [-1, -3, -1, -2, -4, -5]]

maxval = 0

for i in range(4):
    for j in range(4):
        tmpval = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if (tmpval > maxval):
            maxval = tmpval

print(maxval)
    # print (arr[i][j])
        # print (arr[i][j+1])
        # print (arr[i][j+2])
        # print (arr[i+1][j+1])
        # print(arr[i+2][j])
        # print(arr[i+2][j+1])
        # print(arr[i+2][j+2])
        # print('!!!!!!!!!!!!!!!!!!!!!')
