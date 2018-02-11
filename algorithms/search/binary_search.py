# import math
#
#
# def bs(a, x):
#
#     array = a
#     flag = True
#     position = 0
#     position_at_center = math.floor((len(array)) / 2)
#
#     while flag:
#         if x == array[position_at_center]:
#             position = position_at_center
#             flag = False
#         elif x > array[position_at_center]:
#             position_at_center += math.floor((len(array[position_at_center + 1:len(array)])) / 2)
#         elif x < array[position_at_center]:
#             position_at_center -= math.floor((len(array[0:position_at_center])) / 2)
#
#     return position

def Binarysearch(arr, size, value):
    low = 0
    high = size - 1

    while low <= high:
        mid = low + (high - low) / 2  # To	avoid	overflow
        if arr[mid] == value:
            return True
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return False
    

a = [1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 23, 24, 25, 26]
b = [0, 1, 2, 3, 4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16]
# get the position of X
# print(bs(a, 16))
print(Binarysearch(a, 17, 24))
