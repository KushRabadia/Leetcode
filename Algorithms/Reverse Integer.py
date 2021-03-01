class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = (2**31)
        if x <=-l or x >=l-1:
            r= 0
        else:
            r = ""
            if x < 0:
                r += "-"
                x*=-1

            x = str(x)

            for i in x[-1::-1]:
                r += i
            
            r = int(r)

            if r <=-l or r >=l-1:
                r = 0

        return(r)
