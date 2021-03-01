class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones)>1:
            stones.sort(reverse=True)
            stones = [stones[0]-stones[1]]+stones[2:]
    
        return stones[0]
