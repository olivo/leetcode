class Solution(object):
    def findTilt(self, root):
        if root is None:
            return 0

        return self.findTiltRec(root)[1]

    def findTiltRec(self, root):
        if root is None:
            return [0, 0]

        leftRes = self.findTiltRec(root.left)
        rightRes = self.findTiltRec(root.right)

        return [leftRes[0] + rightRes[0] + root.val, leftRes[1] + rightRes[1] + abs(leftRes[0] - rightRes[0])]