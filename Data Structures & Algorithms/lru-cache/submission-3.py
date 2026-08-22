class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {}
        self.used = {}
        self.cap = capacity

    def get(self, key: int) -> int:

        if key not in self.hm:
            return -1
        
        self.used = {k:v+1 for k,v in self.used.items()}
        self.used[key] = 0
        
        return self.hm[key]


    def put(self, key: int, value: int) -> None:
        self.hm[key] = value
        self.used[key] = 0
        self.used = {k:v+1 for k,v in self.used.items()}
        self.used[key] = 0

        if len(self.hm) > self.cap:
            # find index of used with max val
            maxKey, max = None,-1
            for k in self.used:
                if max < self.used[k]:
                    max = self.used[k]
                    maxKey = k
            self.hm.pop(maxKey)
            self.used.pop(maxKey)
            # pop index from used and hm
        
        
