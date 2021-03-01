class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0

        lis =[]
        for i in nums:
            if i != 0:
                lis.append(i)

        for i in lis:
            nums[l]=i
            l+=1

        while l != len(nums):
            nums[l]=0
            l+=1
            
