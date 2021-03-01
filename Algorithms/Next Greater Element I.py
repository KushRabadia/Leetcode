class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        d = dict()
        s = []
        for i in reversed(nums2):
            while s and s[-1] <= i:
                s.pop()
            
            d[i] = -1 if not s else s[-1]
            s.append(i)
            
        return [d[t] for t in nums1]
