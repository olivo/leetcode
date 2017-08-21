class Solution(object):
    def matrixReshape(self, nums, r, c):

        if len(nums) * len(nums[0]) != r * c:
            return nums

        new_nums = [[0 for col in range(c)] for row in range(r)]
        new_r = 0
        new_c = 0

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                new_nums[new_r][new_c] = nums[i][j]

                new_c = new_c + 1

                if new_c >= c:
                    new_c = 0
                    new_r = new_r + 1

        return new_nums