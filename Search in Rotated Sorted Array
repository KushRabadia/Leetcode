class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
    
        while l <= r:
            m = (l+r) // 2
            lv,rv,mv = nums[l],nums[r],nums[m]
            
            if mv == target: return m
            
            if lv <= mv:
                if lv <= target < mv:
                    r = m-1
                else:
                    l = m+1
            else:
                if mv < target <= rv:
                    l = m+1
                else:
                    r = m-1
       
        return -1
