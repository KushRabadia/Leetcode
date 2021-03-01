class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = s.count("A")
        
           
        if a>1 or "LLL" in s:
            return False
        
        return True
