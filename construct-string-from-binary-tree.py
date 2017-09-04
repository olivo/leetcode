class Solution(object):
    def tree2str(self, t):

        res = []

        self.tree2strRec(t, res)

        return ''.join(res)

    def tree2strRec(self, t, res):

        if t is None:
            return

        res.append(str(t.val))

        if t.left is None and t.right is None:
            return

        if t.left is None:
            res.append('()')
        else:
            res.append('(')
            res.append(self.tree2str(t.left))
            res.append(')')

        if t.right is not None:
            res.append('(')
            res.append(self.tree2str(t.right))
            res.append(')')