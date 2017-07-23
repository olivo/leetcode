class Solution(object):
    def arrayPairSum(self, nums):
        res = 0

        nums.sort()

        for index in range(0, len(nums) - 1, 2):
            res += min(nums[index], nums[index + 1])

        return res