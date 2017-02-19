class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x ^ y)[0:].count("1")
