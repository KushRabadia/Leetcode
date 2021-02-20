class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        ans=[]
        P=range(1, m+1)
        
        for i in range(len(queries)):
            toPop=P.index(queries[i])
            ans.append(toPop)
            P.insert(0, P.pop(toPop))
        
        return ans
