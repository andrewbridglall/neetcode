# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if one list is none, return other list
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        # create newList
        newlist = None
        curr = None
        # iterate through list1 and list2 with ptr1, ptr2
        while list1 != None and list2 != None:
            newNode = ListNode()
            if list1.val <= list2.val:
                newNode.val = list1.val
                list1 = list1.next
            else:
                newNode.val = list2.val
                list2 = list2.next
            #if newList None assign head
            if newlist == None:
                newlist = newNode
                curr = newlist
            else:
                curr.next = newNode
                curr = curr.next
            #otherwise insertTail
        # compare vals and add newNode(val) to newList
        # advance ptr of list whose val was added only
        
        # when list1 or list2 runs out, end
        if list1 == None:
            curr.next = list2
        else:
            curr.next = list1

        # update newList ptr to newNode

        # append remaining list to newList
        return newlist
        # return newList