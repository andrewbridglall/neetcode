class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                maxArea = max(maxArea, (j-i)*min(heights[i], heights[j]))
        return maxArea