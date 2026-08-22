class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count elts
        count = defaultdict(int)
        for n in nums:
            count[n] +=1
        # add to array
        arr = [(count[i], i) for i in count]
        # sort arr
        n = len(arr)
        arr.sort(key=lambda x: -x[0])
        
        # return val corresponding to kth most freq elt
        # kth most freq at index n-k
        res = []
        for i in range(k):
            res.append(arr[i][1])
        return res