class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """       
        d_ = ""
        while n > 26:
            j = n%26
            if j == 0:
                d_+=("Z")
                n-=26
            else:
                d_+=(chr(j+64))
            n//=26
        if n > 0:      
            d_+=(chr((n)+64))

        d = d_[::-1]

        return(d)
