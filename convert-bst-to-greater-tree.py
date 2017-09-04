class Solution(object):
    def convertBST(self, root):
        self.convertBSTRec(root, 0)
        return root

    def convertBSTRec(self, root, accum):
        if root is None:
            return 0

        right_count = self.convertBSTRec(root.right, accum)

        previous_root_val = root.val

        root.val += right_count + accum

        left_count = self.convertBSTRec(root.left, root.val)

        return left_count + right_count + previous_root_val