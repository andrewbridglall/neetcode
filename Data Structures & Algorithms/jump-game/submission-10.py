class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy
        # init vars
        n = len(nums)
        goal = n-1
        # iterate thru nums
        for i in range(n-2, -1, -1):
        # update goal
            if i+nums[i] >= goal:
                goal = i
        # return if goal at i 0
        return goal == 0