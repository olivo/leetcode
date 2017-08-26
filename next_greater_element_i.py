class Solution(object):
    def nextGreaterElement(self, findNums, nums):

        greater_map = dict()
        unresolved_numbers = []

        for num in nums:

            while unresolved_numbers and unresolved_numbers[-1] < num:
                greater_map[unresolved_numbers.pop()] = num

            unresolved_numbers.append(num)

        while unresolved_numbers:
            greater_map[unresolved_numbers.pop()] = -1

        res = []
        for num in findNums:
            res.append(greater_map[num])

        return res