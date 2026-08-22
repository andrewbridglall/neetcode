class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # init L, R ptrs, L < R
        L, R = 0, 1
        prevSign = ""
        maxLength = 1
        # iter until R reaches end
        while R < len(arr):
            if arr[R-1] < arr[R] and prevSign != "<":
                maxLength = max(maxLength, R-L+1)
                R +=1
                prevSign = "<"
            elif arr[R-1] > arr[R] and prevSign != ">":
                maxLength = max(maxLength, R-L+1)
                R +=1
                prevSign = ">"
            # elif arr r-1 == arr r
            elif arr[R-1] == arr[R]:
                R +=1
                L = R-1
                prevSign = ""
            # else repeat sign
            else:
                L = R-1
                prevSign = ""
        return maxLength



        # cases
        # prev < next
        # prev > next
        # prev = next
