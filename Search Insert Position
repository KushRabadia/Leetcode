class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0
        last = len(nums)-1
        mid = (first+last)//2

        while first<=last:
            if nums[mid]<target:
                first = mid +1
            elif nums[mid]>target:
                last = mid -1
            else:
                return mid
            mid = (first+last)//2

        return first
        
