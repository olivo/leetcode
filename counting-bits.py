class Solution(object):
    def countBits(self, num):
        
        res = list()
        for temp_num in range(num + 1):
            count = 0
            while temp_num > 0:
                count += temp_num % 2
                temp_num /= 2
            res.append(count)
        return res
