class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # bf - start at every index and traverse as far as possible
        # if return to start ret start index
        n = len(gas)
        for i in range(n):
            # init vars
            start = i
            tail = start
            tank = 0
            # travel
            while True:
                tank += gas[tail]
                tank -= cost[tail]
                if tank >= 0:
                    tail = (tail+1) % n
                else:
                    break
                if tail == start:
                    return start
        # default ret -1
        return -1