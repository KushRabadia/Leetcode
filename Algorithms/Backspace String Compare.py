class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        s, t = [], []
        for i in S:
            if i == "#":
                s and s.pop()
            else:
                s.append(i)
        for i in T:
            if i == "#":
                t and t.pop()
            else:
                t.append(i)
        
        return s==t
