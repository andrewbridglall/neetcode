# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.sortQuick(pairs, 0, len(pairs)-1)

    def sortQuick(self, arr: [], s: int, e: int):
        if e-s+1<=1:
            return arr
        
        pivot = arr[e]
        left = s

        for i in range(s,e+1):
            if arr[i].key < pivot.key:
                arr[left], arr[i] = arr[i], arr[left]
                left +=1
        
        arr[e] = arr[left]
        arr[left] = pivot

        self.sortQuick(arr, s, left-1)
        self.sortQuick(arr, left+1, e)

        return arr