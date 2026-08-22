# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # edge case
        # init data structs
        kmap = defaultdict(list) # starting index -> [start node ref, end node ref]
        # iter thru nodes - track index, node ptr
        index  = 0
        curr = head
        while curr:
            # store start
            if index % k == 0:
                kmap[index].append(curr)
            # store end
            elif index % k == k-1:
                kmap[index - k + 1].append(curr)
            curr = curr.next
            index +=1
        # store start end nodes of k group in map
        # reverse nodes in k group from start to end - only if end exists
        for key in kmap:
            if len(kmap[key]) < 2:
                continue
            start, end = kmap[key]
            # reverse linked list from start to end
            prev = None
            curr = start
            while prev != end:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            # stop after curr == end and curr.next = prev - prev == end
    
        # link nodes together key = group*k - keys are starting indices for each group
        # link group0.start to group1.end and incr group while group + 1 exists
        group = 0
        while (group+1)*k in kmap:
            origin = kmap[group*k][0]
            destination = kmap[(group+1)*k][1] if len(kmap[(group+1)*k]) == 2 else kmap[(group+1)*k][0]
            origin.next = destination
            group +=1
        # return group0 end which is new head of list
        return kmap[0][1] if len(kmap[0]) == 2 else kmap[0][0]