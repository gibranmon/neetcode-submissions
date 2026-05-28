class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while j >= i:
            if  j == i:
                i += 1
                j = len(nums) - 1
            if target == (nums[i] + nums[j]):
                return [i, j]
            j -= 1