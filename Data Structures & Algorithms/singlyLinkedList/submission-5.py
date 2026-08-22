class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        self.size = 0
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i=0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1        

    def insertHead(self, val: int) -> None:
        next = self.head.next
        self.head.next = ListNode(val)
        self.head.next.next = next
        if next == None:
            self.tail = self.head.next
        self.size +=1

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        self.size +=1

    def remove(self, index: int) -> bool: #just fix this
        # set curr to node before node to remove
        curr = self.head
        i = -1
        while curr:
            # find node before node to remove
            if i == index-1:
                break
            curr = curr.next
            i +=1
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            self.size -=1
            return True
        # set curr.next = curr.next.next
        # return false in default case
        return False

    def getValues(self) -> List[int]:
        arr = [0]*self.size
        curr = self.head.next
        i = 0
        while curr:
            arr[i] = curr.val
            curr = curr.next
            i+=1
        return arr
