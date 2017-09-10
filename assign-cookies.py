class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        j = 0
        for i in range(len(g)):
            while j < len(s) and g[i] > s[j]:
                j += 1

            if j >= len(s):
                return i
            else:
                j += 1

        return len(g)