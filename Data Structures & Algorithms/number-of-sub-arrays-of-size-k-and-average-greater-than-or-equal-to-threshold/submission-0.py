class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        for i in range(len(arr)):
            total = 0
            if i+k > len(arr):
                break
            for j in range(i, i+k):

                total += arr[j]
            res = res+1 if total/k >= threshold else res
        return res