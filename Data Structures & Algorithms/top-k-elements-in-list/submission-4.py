class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build count dict
        count = defaultdict(int)
        for n in nums:
            count[n] +=1
        # build and populate arr st. index = freq
        arr = [[] for _ in range((len(nums)+1))] # 0 .... len(nums)
        for n, freq in count.items():
            arr[freq].append(n)
        # build res iter. thru arr right to left until res = len k
        res = []
        for i in range(len(arr)-1, -1, -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res