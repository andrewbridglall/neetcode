class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # build prefix sum arr
        total = 0
        prefix = []
        for n in arr:
            total += n
            prefix.append(total)
        # declare query range helper func
        def queryRange(L, R):
            return prefix[R]-prefix[L-1] if L >=1 else prefix[R]
        # check each sub arr len k
        L = 0
        R = k-1
        res = 0
        while R < len(arr):
            if queryRange(L,R)/k >= threshold:
                res +=1
            L +=1
            R +=1
        return res