class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # bf - try to extend each bar as far as possible
        # init vars
        n = len(heights)
        maxarea = 0
        # iterate thru heights
        for i in range(n):
            # from bar at i, see how far we can extend left and right
            # height l and r >= hieghts i
            l = r = i
            while r+1 < n and heights[r+1] >= heights[i]:
                r+=1
            while l-1 >=0 and heights[l-1] >= heights[i]:
                l-=1
            area = (r-l+1)*heights[i]
            maxarea = max(maxarea, area)
        # return max area rectangle
        return maxarea