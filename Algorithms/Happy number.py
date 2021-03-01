class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l1 =[]

        while n!=1 and n not in l1:
            l1.append(n)
            m = str(n)
            n =0
            for i in m:
                n += int(i)**2

        return n == 1
