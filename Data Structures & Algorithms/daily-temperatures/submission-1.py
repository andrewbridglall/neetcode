class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack soln
        # implement stack
        stack = []
        n = len(temperatures)
        res = [0]*(n)
        # iterate thru temps in reverse
        for i in range(n-1, -1, -1):
            # else temp i >= stack top - pop stack top and push i
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            # if temp i < stack top - set res i, push i to stack
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        # return res
        return res