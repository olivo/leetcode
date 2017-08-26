class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_counter = 0
        current_counter = 0

        for num in nums:
            if num == 0:
                max_counter = max(max_counter, current_counter)
                current_counter = 0
            else:
                current_counter += 1
                max_counter = max(max_counter, current_counter)

        return max_counter