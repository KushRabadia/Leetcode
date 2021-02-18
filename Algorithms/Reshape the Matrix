class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m=len(nums);n=len(nums[0])
        if m*n!=r*c: return nums
        flatten=[]
        for i in nums:
            flatten+=i
        return [flatten[i*c:i*c+c] for i in range(r)]
