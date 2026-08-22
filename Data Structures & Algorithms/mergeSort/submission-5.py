# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergesort(pairs, 0, len(pairs)-1)
    
    def mergesort(self, arr, s, e):
        if e-s+1 <= 1:
            return arr
        
        # calc mid
        mid = (s+e) // 2
        # sort left
        self.mergesort(arr, s, mid)
        # sort right
        self.mergesort(arr, mid+1, e)
        # merge
        self.merge(arr, s, mid, e)
        # return arr
        return arr
    
    def merge(self, arr, s, m, e):
        # store left right in temp arrs
        L = arr[s:m+1]
        R = arr[m+1: e+1]
        # compare left and right and set arr vals
        i,j,k = 0,0, s
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        # i,j oob
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
        
            
