class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<0:
            return False
        binary = '{:032b}'.format(n)
        if binary.count("1") == 1 and binary.index("1")%2!=0:
            return True
        else:
            return False
