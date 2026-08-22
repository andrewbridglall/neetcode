class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # bf - iterate up to max groups in hand
        n = len(hand)
        if n % groupSize != 0:
            return False
        used = set()
        # sort - may not have to
        hand.sort()
        # for each iteration we try to build a group
        # iterate thru hand
        for m in range(n//groupSize):
            curr = -1
            grouplen = 0
            for i in range(n):
        # if group len eq group size break and go to next group
                if grouplen == groupSize:
                    break
        # if card used skip
                if i in used:
                    continue
        # check if i is consecutive to curr
        # if so add to used and update curr
                if curr == -1 or hand[i] == curr + 1:
                    curr = hand[i]
                    used.add(i)
                    grouplen +=1
        # else continue to next i
            if grouplen < groupSize:
                return False
        # if reach end of hand and group len < groupsize - we could not find consecutive cards 
        # so immediately return false
        return True            
