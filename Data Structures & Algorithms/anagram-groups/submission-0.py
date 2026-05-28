class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            is_new = True
            for key in anagrams.keys():
                if self.isAnagram(key, s):
                    anagrams[key].append(s)
                    is_new = False
            if is_new:
                anagrams[s] = [s]
        groups = []
        for k in anagrams:
            groups.append(anagrams[k])
        return groups

        
    def isAnagram(self, a: str, b: str):
        if len(a) != len(b):
            return False

        frec_a, frec_b = {}, {}
        for i in range(len(a)):
            frec_a[a[i]] = frec_a[a[i]] + 1 if a[i] in frec_a else 1
            frec_b[b[i]] = frec_b[b[i]] + 1 if b[i] in frec_b else 1
        return frec_a == frec_b