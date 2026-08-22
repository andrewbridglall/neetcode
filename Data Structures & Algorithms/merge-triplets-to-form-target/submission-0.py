class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # init vars
        n = len(triplets)
        l = 0
        x,y,z = target
        # iterate thru array to find l
        while l < n:
            # check if triplets l leq target
            al, bl, cl = triplets[l]
            if not (al <= x and bl <= y and cl <= z):
                l+=1
                continue
        # iterate thru array from l+1 on and set to r
            merged = False
            for r in range(l+1, n):
                ar, br, cr = triplets[r]
                if not (ar <= x and br <= y and cr <= z):
                    continue
        # when r is suitable, merge l and r and update r
                triplets[r] = [max(al, ar), max(bl, br), max(cl, cr)]
        # set l = r
                l = r
                merged = True
                break
        # after each merge compare to target - if match return true
            if triplets[l] == target:
                return True
            if not merged:
                break
        # default return false
        return False