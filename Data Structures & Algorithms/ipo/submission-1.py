class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # build combined list of [cap[i], profit[i]]
        projects = []
        for i in range(len(profits)):
            projects.append([capital[i], profits[i]])
        # sort list by asc capital
        projects.sort(key=lambda x: (x[0], -x[1]))
        # run dfs and return max capital
        def dfs(i, capMax, proj):
            # base case
            # if len k reached
            if proj == k or i == len(projects):
                return capMax
            # recursive case
            # check if capmax sufficient to include
            include = 0
            if capMax >= projects[i][0]:
                include = dfs(i+1, capMax+projects[i][1], proj+1)
            # include project i
            # skip project i
            skip = dfs(i+1, capMax, proj)
            # remove proj
            # return max
            return max(include, skip)

        # starting cap = w
        return dfs(0, w, 0)
