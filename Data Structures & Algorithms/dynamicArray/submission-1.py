class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = []

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i]=n

    def pushback(self, n: int) -> None:
        # if arr full, resize
        if len(self.arr) == self.capacity:
            self.resize()
        # then push elt
        self.arr.append(n)

    def popback(self) -> int:
        # get elt at last idx
        temp = self.arr[-1]
        # reassign arr to arr w/out last elt
        self.arr = self.arr[:-1]
        # return val
        return temp

    def resize(self) -> None:
        self.capacity *=2

    def getSize(self) -> int:
        return len(self.arr)
    
    def getCapacity(self) -> int:
        return self.capacity
