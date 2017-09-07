class MinMaxRes():
    def __init__(self, min_val, max_val, res):
        self.min_val = min_val
        self.max_val = max_val
        self.res = res

class Solution(object):
    def getMinimumDifference(self, root):
        min_max_res = self.getMinimumDifferenceRec(root)

        return min_max_res.res

    def getMinimumDifferenceRec(self, node):

        if node is None:
            return None

        left_min_max_res = self.getMinimumDifferenceRec(node.left)
        right_min_max_res = self.getMinimumDifferenceRec(node.right)

        min_val = node.val
        max_val = node.val
        res = None

        if left_min_max_res is not None:
            min_val = left_min_max_res.min_val
            res = abs(node.val - left_min_max_res.max_val)

            if left_min_max_res.res is not None:
                res = min(res, left_min_max_res.res)

        if right_min_max_res is not None:
            max_val = right_min_max_res.max_val

            if res is None:
                res = abs(node.val - right_min_max_res.min_val)
            else:
                res = min(res, abs(node.val - right_min_max_res.min_val))

            if right_min_max_res.res is not None:
                res = min(res, right_min_max_res.res)

        return MinMaxRes(min_val, max_val, res)