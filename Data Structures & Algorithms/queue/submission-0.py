class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.size = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        newNode = Node(value)
        prev = self.tail.prev
        self.tail.prev = newNode
        newNode.prev = prev
        prev.next = newNode
        newNode.next = self.tail
        self.size +=1        

    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        next = self.head.next
        self.head.next = newNode
        newNode.next = next
        next.prev = newNode
        newNode.prev = self.head
        self.size +=1        


    def pop(self) -> int:
        if self.isEmpty():
            return -1
        curr = self.tail.prev
        self.tail.prev = curr.prev
        self.tail.prev.next = self.tail
        self.size -=1
        return curr.val


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        curr = self.head.next
        self.head.next = curr.next
        self.head.next.prev = self.head
        self.size -=1
        return curr.val