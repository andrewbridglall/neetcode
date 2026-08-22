class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.arr = []
    
    def get(self, index: int) -> int:
        if index < len(self.arr):
            return self.arr[index]
        else:
            return -1
    
    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            #add to array
            self.arr.append(val)
        elif self.head != None:
            newNode.next = self.head
            self.head = newNode
            self.arr.insert(0,val)
            #add to array 
    
    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        #if tail is None
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        # if tail is not none
        elif self.tail != None:
            self.tail.next = newNode
            self.tail = newNode
            #add to array
        self.arr.append(val)
    
    def remove(self, index: int) -> bool:
        if index < len(self.arr):
            #remove from arr and  get val
            val = self.arr.pop(index)
            #remove from linked list
            curr = self.head
            while curr.next != None:
                if curr.next.val == val:
                    curr.next = curr.next.next
                    break
                
                curr = curr.next
            return True
        else:
            return False

        

    def getValues(self) -> List[int]:
        return self.arr
