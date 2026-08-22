class LRUCache:

    def __init__(self, capacity: int):
        self.deque = collections.deque()
        self.cap = capacity

    def get(self, key: int) -> int:
        # find item
        idx = None
        for i in range(len(self.deque)):
            k,v = self.deque[i]
            if k == key:
                idx = i
                break
        if idx == None:
            return -1
        else:
            k,v = self.deque[idx]
            del self.deque[idx]
            self.deque.append((k,v))
            return v
        

    def put(self, key: int, value: int) -> None:
        # edge case len deque == cap - evict first elt
        # if key already in cache - update val and update
        idx = None
        for i in range(len(self.deque)):
            k,v = self.deque[i]
            if k == key:
                idx = i
                break
        if idx == None:
            if len(self.deque) == self.cap:
                self.deque.popleft()
            # append elt to cache
            self.deque.append((key,value))    
        else:
            del self.deque[idx]
            self.deque.append((key,value))
        
