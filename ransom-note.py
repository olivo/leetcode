class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNoteMap = self.constructCounterMap(ransomNote)
        magazineMap = self.constructCounterMap(magazine)
        
        for letter in ransomNoteMap:
            if letter not in magazineMap or ransomNoteMap[letter] > magazineMap[letter]:
                return False
                
        return True
        
    def constructCounterMap(self, string):
        res = dict()
        for letter in string:
            res[letter] = res.get(letter, 0) + 1
            
        return res
