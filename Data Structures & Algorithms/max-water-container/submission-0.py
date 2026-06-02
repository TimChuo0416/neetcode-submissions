class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            if heights[l] < heights[r]:
                area = (r - l) * heights[l]
                max_area = max(area,max_area)
                l += 1
            else:
                area = (r - l) * heights[r]
                max_area = max(area,max_area)
                r -= 1
        return max_area
            