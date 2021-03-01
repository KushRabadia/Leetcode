class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lis = s.split()
    
        if len(lis)==0:
            return 0
        else:
            return (len(lis[-1]))
