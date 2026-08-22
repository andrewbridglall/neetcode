# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # call recursive mergesort and return
        return self.mergesortRecursive(pairs, 0, len(pairs)-1)

    def mergesortRecursive(self, arr, s, e):
        # base case
        if e-s+1 <= 1:
            return arr
        # recursive case
        m = (s+e)//2
        self.mergesortRecursive(arr, s, m)
        self.mergesortRecursive(arr, m+1, e)
        self.merge(arr, s, m, e)
        return arr

    def merge(self, arr, s, m ,e):
        # store L R in memory
        L = arr[s:m+1]
        R = arr[m+1:e+1]
        # init ptrs i j k
        i = j = 0
        k = s
        # while ptrs not oob
        # compare i j and update k in arr
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i +=1
            else:
                arr[k] = R[j]
                j +=1
            k +=1
        # iterate thru remaining elts
        while i < len(L):
            arr[k] = L[i]
            i +=1
            k +=1
        while j < len(R):
            arr[k] = R[j]
            j +=1
            k +=1
        # nothign to reutrn