# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        # build recursive quicksort soln
        self.quicksortR(pairs, 0, len(pairs)-1)
        # return pairs
        return pairs
    
    def quicksortR(self, arr, s, e):
        # base case
        # if arr is <= len 1 - nothign to sort - return
        if e-s+1 <= 1:
            return
        # recursive case
        # init pivot
        pivot = arr[e].key
        # init ptrs left, i
        left = s
        # for i in range(s,e) not incl end:
        for i in range(s,e):
        # if arr i < pivot:
            if arr[i].key < pivot:
                arr[i], arr[left] = arr[left], arr[i]
                left +=1
        # swap left, i
        # left +=1
        # else: (arr i >= pivot)
        # keep left where it is
        
        # swap left and pivot
        arr[left], arr[e] = arr[e], arr[left]
        # pivot in sorted order
        # quicksort on left
        self.quicksortR(arr, s, left-1)
        # quick sort on right
        self.quicksortR(arr, left+1, e)
