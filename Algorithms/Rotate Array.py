class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        while k > len(nums):
            k-=len(nums)
        tmp = nums[-k:]+nums[:-k]
        nums[:] = tmp
