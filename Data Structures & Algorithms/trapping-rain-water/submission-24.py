class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        volumen = 0

        l = 0
        r = len(height) - 1
        max_l = height[l]
        max_r = height[r]

        while l < r:
            if height[l] < height[r]:
                l += 1
                max_l = max(max_l, height[l])
                volumen += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                volumen += max_r - height[r]

        return volumen