class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        m = 2
        o = 2
        if n == 1:
            result = 1
        elif n == 2:
            result = 2
        else:
            while o != n:
                
                result = l + m
                l = m
                m = result
                o+=1
        
        return result
