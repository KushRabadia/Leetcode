class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        cnt = 0
        for i in s[::-1]:
            n += ((ord(i)-64)*(26**cnt))
            cnt += 1
        return n
