class Solution(object):
    def reverseWords(self, s):
        split_str = s.split(' ')
        res = ''

        for index in range(len(split_str)):
            split_str[index] = split_str[index][::-1]

        return ' '.join(split_str)