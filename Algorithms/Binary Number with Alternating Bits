class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 0:
            nn = n / 2
            if (nn % 2) == (n % 2):
                return False
            n = nn
        return True
