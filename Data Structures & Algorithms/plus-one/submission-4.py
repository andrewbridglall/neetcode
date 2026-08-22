class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # init vars
        n = len(digits)
        # convert digits to number
        num = 0
        mag = 1
        for i in reversed(range(n)):
            num += digits[i]*mag
            mag *= 10
        # add 1 to number
        num +=1
        # convert number to res
        res = []
        while num:
            res.append(num % 10)
            num = num // 10
        res.reverse()
        return res