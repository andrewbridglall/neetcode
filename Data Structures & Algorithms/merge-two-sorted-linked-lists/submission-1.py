# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        newlist = None
        curr = None

        while list1 != None and list2 != None:
            newNode = ListNode()
            if list1.val <= list2.val:
                newNode.val = list1.val
                list1 = list1.next
            else:
                newNode.val = list2.val
                list2 = list2.next

            if newlist == None:
                newlist = newNode
                curr = newlist
            else:
                curr.next = newNode
                curr = curr.next
        
        curr.next = list2 if list1 == None else list1 

        return newlist