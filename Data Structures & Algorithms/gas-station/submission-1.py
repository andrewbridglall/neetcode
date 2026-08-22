class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # optimal - single pass
        # init starting pos
        n = len(gas)
        start = 0
        startRaw = 0
        # traverse
        while True:
            tank = 0
            dest = start
            destRaw = startRaw
            while True:
                tank += gas[dest]
                tank -= cost[dest]
                if tank >= 0:
                    # update dest
                    dest = (dest+1) % n
                    destRaw = destRaw + 1
                else:
                    # fails to make it to next index
                    start = (dest+1) % n
                    startRaw = destRaw + 1
                    break
                if dest == start:
                    return start
            if startRaw >= n:
                break
        # update start if fails
        # ret -1 if no soln
        return -1