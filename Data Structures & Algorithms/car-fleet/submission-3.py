class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # init vars
        n = len(position)
        cars = []
        # build arr position and time to complete
        for i in range(n):
            time = (target - position[i])/speed[i]
            cars.append((position[i], time))
        # sort
        cars.sort()
        # iterate in reverse
        # decr fleet count if time at i-1 <= time at i
        bottleneck = cars[n-1][1]
        fleet = n
        for i in reversed(range(n-1)):
            if cars[i][1] <= bottleneck:
                fleet -=1
            else:
                bottleneck = cars[i][1] 
        # ret fleet count
        return fleet