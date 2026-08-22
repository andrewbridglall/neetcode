class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {}
        self.used = {}
        self.cap = capacity

    def get(self, key: int) -> int:

        if key not in self.hm:
            return -1
        
        self.used[key] = 0
        for k in self.used:
            if k != key:
                self.used[k] +=1
        
        return self.hm[key]


    def put(self, key: int, value: int) -> None:
        # if key exists, update
        # if key dne add
        
        self.hm[key] = value
        self.used[key] = 0

        for k in self.used:
            if k != key:
                self.used[k] +=1
    
        # if size > cap, remove least used key
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
        
        
