class Solution:
    def trap(self, height: List[int]) -> int:
        prefixMax = [0]*len(height)
        suffixMax = [0]*len(height)
        currmax = 0
        for i in range(len(height)):
            prefixMax[i] = currmax
            currmax = max(currmax, height[i])
        currmax = 0
        for i in range(len(height)-1, -1, -1):
            suffixMax[i] = currmax
            currmax = max(currmax, height[i])
        print(prefixMax)
        print(suffixMax)
        res = 0
        for i in range(len(height)):
            water = min(prefixMax[i], suffixMax[i]) - height[i]
            res += max(water, 0)
        return res