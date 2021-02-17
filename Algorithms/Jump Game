class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums[0]>len(nums)-1:
            return True
        j = 0
        for i in (nums[-2::-1]):
            j += 1
            if i - j >= 0: j = 0
        return j <= 0
