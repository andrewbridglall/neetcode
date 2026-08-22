class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, currSet):
            if len(currSet) == k:
                res.append(currSet.copy())
                return
            if i == n+1:
                return
            currSet.append(i)
            dfs(i+1, currSet)
            currSet.pop()
            dfs(i+1, currSet)
        dfs(1, [])
        return res
