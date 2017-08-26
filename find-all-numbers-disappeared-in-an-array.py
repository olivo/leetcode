class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] *= -1

        res = []

        for index in range(len(nums)):
            if nums[index] > 0:
                res.append(index + 1)

        return res