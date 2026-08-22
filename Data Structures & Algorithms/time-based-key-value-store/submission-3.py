class TimeMap:

    def __init__(self):
        # hashmap to store list of values and timestamps
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # binary search until find t <= timestamp
        items = self.tmap[key]
        l,r = 0, len(items)-1
        closestV = ""
        while l <= r:
            # calc midpoint
            m = (l+r)//2
            t, v = items[m]
            # compare target timestamp to midpoint timestamp
            # if target > midpoint
            if timestamp > t:
                l = m+1
                closestV = v
            # if target < midpoint
            elif timestamp < t:
                r = m-1
            # if target == midpoint
            else:
                return v
        # return closest value st t leq target
        return closestV

