class Solution(object):
    def findTheDifference(self, s, t):
        counter = dict()
        for ch in s:
            if ch in counter:
                counter[ch] = counter[ch] + 1
            else:
                counter[ch] = 1
        for ch in t:
            if ch in counter and counter[ch] > 0:
                counter[ch] = counter[ch] - 1
            else:
                return ch
