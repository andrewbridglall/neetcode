class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*(n)

        target = n-1
        for i in range(n-1, -1, -1):
            # can we reach target from i
            # if so update target and mark true
            # else false and continue
            if nums[i] >= target - i:
                target = i
                dp[i] = True
            else:
                dp[i] = False
        return dp[0]
