class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        hmap = defaultdict(int)
        for n in nums:
            hmap[n] +=1
        return True if max(hmap.values()) > 1 else False