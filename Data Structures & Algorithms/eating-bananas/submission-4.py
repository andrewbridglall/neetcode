class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # init vars
        # get max val in arr
        maxk = max(piles)
        mink = maxk
        # binary search k = 1... max
        l, r = 1, maxk
        while l <= r:
            midk = (l+r)//2
            hours = 0
            for p in piles:
                t = p//midk + 1 if p % midk else p//midk
                hours += t

            # calc hours
            if hours > h:
                l = midk+1
            else:
                mink = min(mink, midk)
                r = midk -1
        # return min k

        return mink