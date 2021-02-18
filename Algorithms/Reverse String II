class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        d = ""
        i = 0
        r = True
        while i<len(s):
            p = s[i:i+k]
            if r:
                d+=p[::-1]
            else:
                d+=p
            i+=k
            r = not r
        
        return d
       
