class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_set = set()
        num_index = dict()
        
        for index in range(0, len(nums)):
            num = nums[index]
            num_set.add(num)
            num_index[num] = index
            
        for index in range(0, len(nums)):
            num = nums[index]
            if (target - num) in num_set and index != num_index[target - num]:
                return index, num_index[target - num]
                
        return -1
