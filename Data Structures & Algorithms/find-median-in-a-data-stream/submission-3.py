class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        # insert number to maintain sorted order
        if not self.nums:
            self.nums.append(num)
            return
        for i in range(len(self.nums)+1):
            if i == len(self.nums):
                self.nums.append(num)
                return
            if num < self.nums[i]:
                self.nums.insert(i, num)
                return

    def findMedian(self) -> float:
        mid = (0 + len(self.nums)-1)//2
        if len(self.nums) %2 == 0:
            return (self.nums[mid] + self.nums[mid+1])/2
        else:
            return self.nums[mid]