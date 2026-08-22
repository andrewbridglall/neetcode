class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currsum = 0
        prefixMap = { 0:1 }

        for n in nums:
            # update currsum
            currsum += n
            # if currsum - k in hashmap, add val to res
            res += prefixMap.get(currsum-k, 0)
            # add new sum to hashmap
            prefixMap[currsum] = prefixMap.get(currsum, 0) + 1
        return res
