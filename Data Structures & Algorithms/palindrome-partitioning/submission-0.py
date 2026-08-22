class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # bf - create all possible list of substr, check if substr palindromic
        # init vars
        res = []
        n = len(s)
        currset = []
        # make dfs
        def dfs(i):
            # base case
            # if i == n, check if all substr in currset palindromic
            if i == n:
                # check if all substr palindromic
                for substr in currset:
                    l, r = 0, len(substr) -1
                    while l < r:
                        if substr[l] != substr[r]:
                            return
                        l +=1
                        r -=1
                # if make it to end - didn't return - all substr palindromic
                res.append(currset.copy())
                return
            # recursive case
            # add i to existing substr
            lastsub = currset.pop()
            currset.append(lastsub+s[i])
            dfs(i+1)

            # reset
            currset.pop()
            currset.append(lastsub)
            # start new substr with i
            currset.append(s[i])
            dfs(i+1)

            currset.pop()
        # run dfs
        currset.append(s[0])
        dfs(1)
        # ret res
        return res
        