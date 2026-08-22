class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        res = 0
        total = 0

        for R in range(len(arr)):
            if R-L+1 > k:
                total -= arr[L]
                L+=1
            total += arr[R]
            if R-L+1 == k and total/k >= threshold:
                res+=1
        return res