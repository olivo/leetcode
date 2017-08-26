class Solution(object):
    def detectCapitalUse(self, word):
        return word == word.upper() or word == word.lower() or word == word[0].upper() + word[1 :].lower()