class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        result=0
        
        for c in zip(*A):
            if list(c)!=sorted(c):
                result+=1
        
        return result
