class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        prev = self.tail.prev
        next = self.tail
        self.addNode(prev, Node(value), next)

    def appendleft(self, value: int) -> None:
        prev = self.head
        next = self.head.next
        self.addNode(prev, Node(value), next)

    # append helper
    # can append given prev, next, newnode
    def addNode(self, prev, newNode, next):
        prev.next = newNode
        newNode.next = next
        next.prev = newNode
        newNode.prev = prev


    def pop(self) -> int:
        # edge case
        if self.isEmpty(): return -1
        next = self.tail
        prev = next.prev.prev
        return self.popNode(prev, next) 

    def popleft(self) -> int:
        # edge case
        if self.isEmpty(): return -1
        prev = self.head
        next = prev.next.next
        return self.popNode(prev, next) 
        
    # pop helper
    def popNode(self, prev, next):
        val = prev.next.val
        prev.next = next
        next.prev = prev
        return val