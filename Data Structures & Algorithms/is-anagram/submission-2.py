class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t = list(t)
        for letter in s:
            index_t = -1
            try:
                index_t = t.index(letter)
            except ValueError:
                return False
            t.pop(index_t)
        return len(t) == 0
        
