class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # convert digits to num
        n = len(digits)
        num = 0
        order = 1
        for i in range(n-1, -1, -1):
            num += digits[i] * order
            order *= 10
        # add 1 to num
        num += 1
        print(num)
        # convert num to digits
        # overwrite digits
        res = []
        while num:
            res.append(num % 10)
            num //= 10
        res.reverse()
        return res