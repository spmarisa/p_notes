def sumofsquares(m):

    if m < 0:
        return False

    for i in range(1, m):
        a = i
        b = m - i
        if (int(a**0.5)**2 == a) and (int(b**0.5)**2 == b):
            return True

    return False



print(sumofsquares(17))