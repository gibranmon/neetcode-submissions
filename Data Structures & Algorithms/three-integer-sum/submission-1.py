class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()

        res = []
        for i, n in enumerate(nums):
            l = 0
            r = len(nums) - 1
            while l < r:
                if l == i:
                    l += 1
                if r == i:
                    break
                sum_r = n + nums[l] + nums[r]
                if sum_r < 0:
                    l += 1
                if sum_r > 0:
                    r -= 1
                if sum_r == 0:
                    array_r = [n, nums[l], nums[r]]
                    array_r.sort()
                    if array_r not in res:
                        res.append(array_r)
                    l += 1

        return res

        