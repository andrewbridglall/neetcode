class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # init ptrs
        # init vars max
        maxarea = 0
        l,r = 0, len(heights)-1
        # while l < r
        while l < r:
            currarea = min(heights[l], heights[r])*(r-l)
            maxarea = max(maxarea, currarea)
        # calc area, compar eto max
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        # update ptrs
        # return max
        return maxarea