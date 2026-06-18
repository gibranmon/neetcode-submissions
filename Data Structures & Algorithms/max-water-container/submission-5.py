class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 2:
            return 0

        max_a = 0
        
        f = 0
        l = len(heights) - 1

        while f < l:
            b = l - f
            max_fill = min(heights[f], heights[l])
            max_a = max(max_a, b * max_fill)
            if heights[f] < heights[l]:
                f += 1
            else:
                l -= 1
            print(f, l)

        return max_a
