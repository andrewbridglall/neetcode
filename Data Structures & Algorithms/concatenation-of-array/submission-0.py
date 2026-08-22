class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # init new arr of size 2n
        concat_arr = [0]*(2*len(nums))
        # for index, num in nums:
        for index, num in enumerate(nums):
            # set vals
            concat_arr[index] = num
            concat_arr[index + len(nums)] = num
        return concat_arr