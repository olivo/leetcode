class Solution(object):
    def findTarget(self, root, k):

        required_value = set()

        return self.findTargetRec(root, k, required_value)

    def findTargetRec(self, root, k, required_value):
        if root is None:
            return False

        if root.val in required_value:
            return True

        required_value.add(k - root.val)

        return self.findTargetRec(root.left, k, required_value) or self.findTargetRec(root.right, k, required_value) 