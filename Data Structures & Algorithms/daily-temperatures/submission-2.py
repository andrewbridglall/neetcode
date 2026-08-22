class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # implement with stack in reverse
        # init vars
        n = len(temperatures)
        stack = []
        res = [0]*n
        # populate res
        for i in reversed(range(n)):
            # compare temp i to top of stack
            # if less than top set res to diff
            while stack and temperatures[i] >= stack[-1][1]:
                stack.pop()
            if stack:
                index, _ = stack[-1]
                res[i] = index-i
            else:
                res[i] = 0
            # else curr temp >= top - pop from stack
            # if stack empty, then there is no temp greater than curr temp - ret 0
            # add temp to stack
            stack.append((i, temperatures[i]))

        return res