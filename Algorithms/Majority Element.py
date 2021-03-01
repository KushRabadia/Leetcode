class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        if(len(nums)%2==0):
            return nums[((length-1) // 2 + 1)]
        else:
            return nums[(length -1) // 2]
            
