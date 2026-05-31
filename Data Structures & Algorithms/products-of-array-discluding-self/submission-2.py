class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = {}
        for i, v in enumerate(nums):
            res[i] = 1
        
        for i, v in enumerate(nums):
            for j, n in enumerate(nums):
                if i != j:
                    res[j] *= v
        
        return list(res.values())