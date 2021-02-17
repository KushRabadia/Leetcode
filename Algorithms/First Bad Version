# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n, floor=0):
        """
        :type n: int
        :rtype: int
        """
        if n == floor:
            return n
        
        middle = floor + (n - floor -1) // 2 + 1
        
        if isBadVersion(middle):
            if middle - 1 <= floor:
                return middle
            return self.firstBadVersion(middle, floor=floor)
        
        return self.firstBadVersion(n, floor=middle)
            
        
