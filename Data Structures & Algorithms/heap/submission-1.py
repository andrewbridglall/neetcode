class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        # append val to end of heap
        self.heap.append(val)
        # starting at last ind while i > 1
        i = len(self.heap)-1
        # percolate up
        while i > 1 and self.heap[i] < self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2



    def pop(self) -> int:
        # if heap is empty return none
        if len(self.heap) < 2:
            return -1
        # if heap is len 1 pop
        if len(self.heap) == 2:
            return self.heap.pop()
        # store res of top of heap
        # top = last element
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        # while a child exists - percolate down
        self.heapHelper(i)
        return res

    def heapHelper(self, i):
        while 2*i < len(self.heap):
            if 2*i+1 < len(self.heap) and \
            self.heap[2*i+1] < self.heap[2*i] and \
            self.heap[i] > self.heap[2*i+1]:
                self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                i = 2*i+1
            elif self.heap[i] > self.heap[2*i]:
                self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                i = 2*i
            else:
                break
        # - if right child in bound, is min of right, left children, parent > child
        # swap parent and right child
        # update index to right child
        # else if parent > left child
        # swap parent and left child and udpate index
        # else heap prop satisfied break
        # return res

    def top(self) -> int:
        if len(self.heap) < 2:
            return -1
        return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        # given input array
        if not nums:
            return None
        nums.append(nums[0])
        self.heap = nums
        # start at first nonleaf node
        curr = (len(self.heap)-1)//2
        # while curr > 1
        # - set i = curr (starting point)
        # - percolate down
        while curr > 0:
            i = curr
            self.heapHelper(i)
            curr -=1

        
        