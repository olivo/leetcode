class Solution(object):
    def firstUniqChar(self, s):
        occurrences = dict()

        for c in s:
            if c not in occurrences:
                occurrences[c] = 0

            occurrences[c] += 1

        for index in range(len(s)):
            c = s[index]

            if occurrences[c] == 1:
                return index

        return -1