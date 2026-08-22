class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # bf
        # init vars
        n = len(temperatures)
        res = [0 for _ in range(n)]
        # iterate thru temps
        for i in range(n):
            for j in range(i+1, n):
                if temperatures[i] < temperatures[j]:
                    res[i] = j-i
                    break
        # for each temp find next largest temp
        # calc index distance excl
        # append to res
        # return res
        return res