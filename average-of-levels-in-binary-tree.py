class Solution(object):
    def averageOfLevels(self, root):

        if root is None:
            return []

        visited = set()
        level_values = dict()

        s = [(root, 0)]

        while s:
            node, level = s.pop()

            if node not in visited:
                visited.add(node)

                if level not in level_values:
                    level_values[level] = []

                level_values[level].append(node.val)

                if node.left is not None:
                    s.append((node.left, level + 1))

                if node.right is not None:
                    s.append((node.right, level + 1))

        res = []
        level = 0

        while level in level_values:
            sum = 0
            for node in level_values[level]:
                sum += node

            res.append(float(sum) / len(level_values[level]))

            level += 1

        return res