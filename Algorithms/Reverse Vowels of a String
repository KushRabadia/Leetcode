class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        start=0
        end=len(s)-1
        result=list(s)
        s=s.lower()
        d=set(["a", "e", "i","o","u"])
        print(s)
        while start<end:
            while start<end and (not s[start] in d ):
                start+=1
            while start<end and (not s[end] in d):
                end-=1
            result[start],result[end]=result[end],result[start]
            start+=1
            end-=1
            
        return "".join(result)
