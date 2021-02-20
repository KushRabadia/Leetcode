class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        departure = set()
        
        for i in paths:
            departure.add(i[0])
            
        for i in paths:
            if i[1] not in departure:
                return i[1]
