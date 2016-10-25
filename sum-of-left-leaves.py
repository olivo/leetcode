class Solution(object):
    def sumOfLeftLeaves(self, root):
        if root == None:
            return 0
        if root.left == None:
            return self.sumOfLeftLeaves(root.right)
        else:
            tmp = 0
            if root.left.left == None and root.left.right == None:
                tmp = root.left.val
            return tmp + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
