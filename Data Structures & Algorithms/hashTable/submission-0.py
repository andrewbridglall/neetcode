class Pair:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = [None]*self.capacity
        self.size = 0
        
    def insert(self, key: int, value: int) -> None:
        # index = hash(key)
        # check if key already exists
        if self.get(key) != -1:
            index = self.hash(key)
            while self.table[index] != None:
                if self.table[index].key == key:
                    self.table[index].val = value
                    return
                index = index +1
                index = index % self.capacity
        else:
            # if here, we check if we need to resize
                
            index = self.hash(key)
            while self.table[index] != None:
                index = index +1
                index = index % self.capacity
            
            self.table[index] = Pair(key,value)
            self.size +=1

            if 2*self.size >= self.capacity:
                self.resize()
        # find empty space to add key
        # edge case - key exists
        # edge case - if size == cap, resize table

    def get(self, key: int) -> int:
        # key --> (hash) index
        index = self.hash(key)
        count = 0
        # find index
        while self.table[index] != None:
            if self.table[index].key == key:
                return self.table[index].val
            if count == self.size:
                break
            index = index +1
            index = index % self.capacity
            count +=1
        return -1
        # if check all indices not found

    def hash(self, key: int) -> int:
        return key % self.capacity

    def remove(self, key: int) -> bool:
        if self.get(key) == -1:
            return False
        index = self.hash(key)
        while self.table[index] != None:
            if self.table[index].key == key:
                break
            index = index +1
            index = index % self.capacity
        self.table[index] = None
        self.rehash()
        return True


    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        # make new table with 2*cap
        self.capacity = 2*self.capacity
        # set self.table = newtable
        # add oldtable elts to newtable
        self.rehash()


    def rehash(self) -> None:
        newTable = [None]*self.capacity
        self.size = 0
        # store curr table
        oldTable = self.table
        # print(oldTable)
        self.table = newTable
        for elt in oldTable:
            if elt:
                self.insert(elt.key,elt.val)

