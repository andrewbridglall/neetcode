class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for n in nums:
            prod *=n
        output = []
        for i in range(len(nums)):
            if nums[i] == 0:
                # calc product from scratch
                p = 1
                for j in range(len(nums)):
                    if j !=i:
                        p *= nums[j]
                output.append(p)
            else:
                output.append(prod//nums[i])
        return output