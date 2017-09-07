class Solution(object):
    def intersection(self, nums1, nums2):
        set_nums1 = set(nums1)

        res = set()

        for num in nums2:
            if num in set_nums1:
                res.add(num)

        return list(res)