class Solution(object):
    def findComplement(self, num):
        binNum = format(num, 'b')
        binNum = binNum[binNum.find('1') : ]
        
        return int(binNum.translate(string.maketrans('01', '10')), 2)
