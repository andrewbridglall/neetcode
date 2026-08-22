class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currsum = 0
        prefixMap = { 0:1 }

        for n in nums:
            # update currsum
            currsum += n
            # add new sum to hashmap
            if currsum-k in prefixMap:
                res += prefixMap[currsum-k]
            prefixMap[currsum] = prefixMap[currsum] + 1 if currsum in prefixMap else 1
            # if currsum - k in hashmap, add val to res
        return res
