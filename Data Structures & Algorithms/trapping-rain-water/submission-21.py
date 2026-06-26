class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        volumen = 0

        i = 1

        while i < len(height):
            l = i - 1
            r = i + 1
            max_l = 0
            max_r = 0
            while l >= 0:
                max_l = max(max_l, height[l])
                l -= 1
            
            while r < len(height):
                max_r = max(max_r, height[r])
                r += 1
            
            
            if height[i] >= min(max_l, max_r):
                i += 1
                continue
            
            volumen += min(max_l, max_r) - height[i]
            i += 1

        return volumen