class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * self.capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i]=n

    def pushback(self, n: int) -> None:
        # if run out of space - resize
        if self.length == self.capacity:
            self.resize()
        # add elt to back
        self.arr[self.length] = n
        # incr len by 1
        self.length +=1

    def popback(self) -> int:
        # rm elt from back
        last_val = self.arr[self.length-1]
        self.arr[self.length-1] = 0
        self.length -=1
        return last_val
        # replace with zero
        # return val
        # decr len by 1

    def resize(self) -> None:
        # increase cap x2
        self.capacity *=2
        newarr = [0]*self.capacity
        for i in range(self.length):
            newarr[i] = self.arr[i]
        
        self.arr = newarr
        # gen new arr and copy vals
        # reassign arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
