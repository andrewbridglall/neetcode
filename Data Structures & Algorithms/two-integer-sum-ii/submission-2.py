class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # init l,r
        l,r = 0, len(numbers)-1
        # l r not same
        while l < r:
        # if sum too big r-=1
        # if sum too small l+=1
        # if == break
        # add 1 to l ,r
            if numbers[l]+numbers[r] > target:
                r -=1
            elif numbers[l]+numbers[r] < target:
                l +=1
            else:
                # equal
                break
        # ret
        return [l+1, r+1]