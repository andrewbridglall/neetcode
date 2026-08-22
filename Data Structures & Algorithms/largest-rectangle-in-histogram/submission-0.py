class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # bf - calc area for every subarray
        # init vars
        maxarea = 0
        n = len(heights)
        # iterate thru arr
        for i in range(n):
        # init min at start of each iter
            minheight = heights[i]
            for j in range(i,n):
                # update min
                minheight = min(minheight, heights[j])
                area = minheight * (j-i+1)
                # update maxarea
                maxarea = max(maxarea, area)
                
        # return maxarea
        return maxarea