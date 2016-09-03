class Solution(object):
    def addDigits(self, num):
        if num < 10:
            return num
        res = 0
        for c in str(num):
            res += ord(c) - ord('0')
        return self.addDigits(res)
