class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            minHeight = min(heights[l], heights[r])
            area = (r - l) * minHeight
            maxArea = max(area, maxArea)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            
        return maxArea
