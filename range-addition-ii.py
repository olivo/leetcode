class Solution(object):
    def maxCount(self, m, n, ops):

        if not ops:
            return m * n

        min_rows = sys.maxint
        min_cols = sys.maxint

        for op in ops:
            min_rows = min(min_rows, op[0])
            min_cols = min(min_cols, op[1])

        return min_rows * min_cols