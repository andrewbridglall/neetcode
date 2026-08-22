class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # store max L, max R in arr
        heightL = [0]*n
        heightR = [0]*n
        
        maxL = 0
        for i in range(n):
            maxL = max(maxL, height[i])
            heightL[i] = maxL
        
        maxR = 0
        for i in reversed(range(n)):
            maxR = max(maxR, height[i])
            heightR[i] = maxR
        # calc total area
        totalarea = 0
        for i in range(n):
            totalarea += min(heightL[i], heightR[i]) - height[i]
        return totalarea