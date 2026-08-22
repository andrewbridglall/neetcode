# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # make recursive mergesort func with params: arr, start, end
        # make merge func that combines L, R sorted subarrays
        return self.sortMerge(pairs, 0, len(pairs)-1)
    
    def sortMerge(self, arr: List[Pair], start: int, end: int):
        # if len arr <=1 return arr
        if end-start+1<=1:
            return arr
        mid = (start + end)//2
        self.sortMerge(arr, start, mid)
        self.sortMerge(arr, mid+1, end)

        self.merge(arr, start, end, mid)
        return arr
        # calc midpoint
        # sort left half
        # sort right half
        # merge left and right halfs
        # return arr
    
    def merge(self, arr: List[Pair], start: int, end: int, mid: int):
        # store copy of L, R subarrays given ptrs
        L = arr[start:mid+1]
        R = arr[mid+1:end+1]

        i = 0
        j = 0
        k = start

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i +=1
            else:
                arr[k] = R[j]
                j +=1
            k +=1
        
        while i < len(L):
            arr[k] = L[i]
            i +=1
            k +=1
        
        while j < len(R):
            arr[k] = R[j]
            j +=1
            k +=1
        # set starting indices
        # while both ptrs valid - update arr and update ptrs
        # when one arr reaches end - add remaining subarr vals to arr
        # return arr
