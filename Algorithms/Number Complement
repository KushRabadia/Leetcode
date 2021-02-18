class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        count = 0
        while num != 0:
            if num&1 == 0:
                res += 1<<count
            count += 1
            num >>= 1
        return res
