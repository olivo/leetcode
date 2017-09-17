class Solution(object):
    def findRelativeRanks(self, nums):
        sorted_nums = sorted(nums, reverse=True)
        rank_map = dict()

        for index in range(len(sorted_nums)):
            if index == 0:
                val = "Gold Medal"
            elif index == 1:
                val = "Silver Medal"
            elif index == 2:
                val = "Bronze Medal"
            else:
                val = str(index + 1)
            rank_map[sorted_nums[index]] = val

        res = []

        for num in nums:
            res.append(rank_map[num])

        return res