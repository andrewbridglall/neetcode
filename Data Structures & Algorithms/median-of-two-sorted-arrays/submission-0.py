class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # bf
        # concat arrays
        nums1.extend(nums2)
        # sort
        nums1.sort()
        k = len(nums1)
        first = 0
        last = k-1
        mid = (first+last)//2
        # if odd - take middle
        if k % 2:
            return nums1[mid]
        # if even - get middle two and average
        else:
          return (nums1[mid]+nums1[mid+1])/2  
