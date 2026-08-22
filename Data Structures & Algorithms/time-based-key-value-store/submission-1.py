class TimeMap:

    def __init__(self):
        # init hashmap key -> list
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # append tuple of value, timestmamp to kv store
        self.tmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # get list from key
        mylist = self.tmap[key]
        # implement binary serach to find most recent val given timestamp
        l, r = 0, len(mylist)-1
        res = "" # default
        while l <= r:
            # calc mid
            m = (l+r)//2
            # check if timestamp is valid or not
            v,t = mylist[m]
            # move ptrs accordingly
            if t <= timestamp:
                # update val v
                res = v
                # move range up l = m+1
                l = m+1
            else: # t > timestamp - not valid
                # move range down r = m -1
                r = m-1
        return res