import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pileMax = max(piles)
        s, e = 1, pileMax
        res = -1
        while s <= e:
            k = s+(e-s)//2
            # calc total time to complete piles
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/k)
            if total_time > h:
                s = k+1
            else:
                res = k
                e = k-1
        return res