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
            if len(res) == k:
                break
            # val at pos is empty
            if not arr[i]:
                continue
            # val at pos is nonemtpy
            # append nums to res
            for num in arr[i]:
                if len(res) < k:
                    res.append(num)
                else:
                    break
        # return res
        return res