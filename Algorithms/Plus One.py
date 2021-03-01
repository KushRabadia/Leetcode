class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = 0
        i= len(digits)
        for v in digits:
            if i ==1:
                ans+=v
            else:
                ans += v * ((10 **(i-1)))
                i-=1
        return [int(i) for i in str(ans+1)]
