import math
def IsPrime(A):
        flag = True
        if A == 1:
            return False
        for t in range(2,int(math.sqrt(A))+1):
            if A%t == 0:
                flag = False
                break
        return flag

class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        op = []
        all_primes = []

        for i in range(2, A):
            if IsPrime(i):
                all_primes.append(i)

        flag = False

        for i in all_primes:
            first_number = i
            for j in all_primes
                second_number = j
                if first_number + second_number == A:
                    op.append(first_number)
                    op.append(second_number)

                    flag = True
                    break

            if flag == True:
                break
        return op
