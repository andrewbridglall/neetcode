class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, currset):
            # base case
            if len(currset) == k:
                res.append(currset.copy())
                return
            # recusrive case
            for j in range(i, n+1):
                currset.append(j)
                dfs(j+1, currset)
                currset.pop()
        dfs(1, [])
        return res
