import sys
class Solution(object):
    def getSum(self, a, b):
        if a < 0 and b < 0:
            neg = True
            a = abs(a)
            b = abs(b)
        elif (abs(a) > abs(b) and a < 0) or (abs(a) < abs(b) and b < 0):
            a = -a
            b = -b
            neg = True
        else:
            neg = False
        
        res = 0
        carry = 0
        for index in range(sys.getsizeof(res)):
            val = (a & 1) ^ (b & 1) ^ carry
            res = res | (val << index)
            carry = (a & b & 1) | (a & carry & 1) | (b & carry & 1)
            a = a >> 1
            b = b >> 1
        if neg:
            return -res
        else:
            return res
