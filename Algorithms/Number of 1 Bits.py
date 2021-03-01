class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = '{0:032b}'.format(n)
        count = 0 
        for i in n:
            if i == "1":
                count+=1
        
        return count
        
