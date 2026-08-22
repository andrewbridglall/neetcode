class Solution:
    def countBits(self, n: int) -> List[int]:
        # init vars
        output = []
        # iterate through nums from 0 to n incl
        for num in range(n+1):
        # count 1 bits and append to output
            count = 0
            # bitmask 1 at every bit pos
            for i in range(32):
                if num & (1 << i):
                    count +=1
            # compare to num
            output.append(count)
        # return output
        return output