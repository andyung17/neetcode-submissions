class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        start = 0
        end = len(heights) - 1
        water_amount = 0
        
        while start < end:

            height = min(heights[start], heights[end]) 
            if height * (end - start) > water_amount:
                water_amount = height * (end - start)

            if heights[start] < heights[end]:
                start = start + 1
            elif heights[start] > heights[end]:
                end = end - 1
            else:
                start = start + 1
        
        return water_amount