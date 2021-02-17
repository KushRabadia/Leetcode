class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        del nums1[m: ]
        while j<n and i<m:
            if nums1[i] > nums2[j]:
                nums1.insert(i,nums2[j])
                m+=1
                j += 1
            i += 1


        if j != n:
            nums1.extend(nums2[j:]) 
