class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #1 = 0b0001
        #4 = 0b0100
        res = 0
        while x>0 or y>0:
            if x&1 != y&1:
                res+=1
            x = x>>1
            y = y>>1
        return res
