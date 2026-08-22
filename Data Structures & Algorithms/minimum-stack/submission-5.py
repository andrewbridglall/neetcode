class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MinStack:

    def __init__(self):
        self.dummy = Node(-1)
        self.mindummy = Node(-1)
        
    def push(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.dummy.next
        self.dummy.next = newNode

        if not self.mindummy.next:
            minVal = val
        else:
            minVal = min(self.getMin(), val)
        minNode = Node(minVal)
        minNode.next = self.mindummy.next
        self.mindummy.next = minNode
        

    def pop(self) -> None:
        self.dummy.next = self.dummy.next.next
        self.mindummy.next = self.mindummy.next.next

    def top(self) -> int:
        return self.dummy.next.val

    def getMin(self) -> int:
        return self.mindummy.next.val
