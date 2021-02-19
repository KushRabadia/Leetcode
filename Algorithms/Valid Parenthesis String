class Solution(object):

    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open = 0
        
        
        for i in s:
            if i == '(' or  i == '*':
                open+=1
            else:
                open-=1
                
            if open<0:
                return False
            
        if open == 0:
            return True
        close = 0
        print(open,close)
        for i in range(len(s)-1,-1,-1):
            j = s[i]
            if j == ')' or  j == '*':
                close+=1
            else:
                close-=1
            if close<0:
                return False
        
        return True
