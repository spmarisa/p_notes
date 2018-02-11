def is_uniq(a):
    # considering ascii chars
    if len(a) > 128:
        return False

    array = [False] * 128

    for i in a:
        key = ord(i)
        if array[key] == True:
            return False
        else:
            array[key] = True

    return True


a = 'abcdefghijklmnona'
print(is_uniq(a))

