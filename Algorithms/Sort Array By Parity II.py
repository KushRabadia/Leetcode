class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = [None]*len(A)
        
        i = 0
        j = 1
        
        for k in A:
            if k%2==0:
                B[i]=k
                i+=2
            else:
                B[j]=k
                j+=2
        
        return B
