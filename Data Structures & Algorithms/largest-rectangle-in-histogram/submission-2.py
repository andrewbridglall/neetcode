class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # optimal
        # init vars
        n = len(heights)
        # precompute left bound
        leftBound = [-1]*n
        stack = []
        for i in range(n):
            # before we add height to stack, check if top of stack >= curr height ie, we can extend
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            # top of stack remaining is left bound
            if stack:
                leftBound[i] = stack[-1]
            # add heights to stack
            stack.append(i)

        # precompute right bound
        rightBound = [n]*n
        stack = []
        for i in range(n-1, -1, -1):
            # same as left
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightBound[i] = stack[-1]
            stack.append(i)
        # iterate thru heights and calc maxarea
        maxarea = 0
        for i in range(n):
            left = leftBound[i]+1
            right = rightBound[i]-1
            maxarea = max(maxarea, (right-left+1)*heights[i])

        # return maxarea
        return maxarea