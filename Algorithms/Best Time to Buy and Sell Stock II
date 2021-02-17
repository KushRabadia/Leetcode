class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b= 0
        s= 0
        i = 0
        total = 0
        l_ =  len(prices)-1
        while i < l_:
            while (i < l_) and (prices[i]>=prices[i+1]):
                i+=1
            b = prices[i]

            while (i < l_) and (prices[i]<=prices[i+1]):
                i+=1
            s = prices[i]

            total+=(s-b)

        return total
