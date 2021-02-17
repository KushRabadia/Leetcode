class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        n = len(x)
        m = n//2
        a = x[:m]
        if n % 2 == 1:
            m+=1
        b = x[:m-1:-1]

        if a == b:
            result = True
        else:
            result = False

        return(result)
