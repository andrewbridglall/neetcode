# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        if not pairs:
            return res
        res.append(pairs.copy())
        for i in range(1, len(pairs)):
            j = i-1
            while j > -1:
                # compare j and j+1
                if pairs[j].key > pairs[j+1].key:
                    pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                    j -=1
                else:
                    break
            res.append(pairs.copy())
        return res