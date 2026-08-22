class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        if not self.nums:
            return -1

        # even len
        mid = (0 + len(self.nums)-1)//2
        if len(self.nums) %2 == 0:
            return (self.nums[mid] + self.nums[mid+1])/2
        else:
            return self.nums[mid]