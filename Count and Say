class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        str1 = "1"
        count = 0

        for i in range(n-1):
            tmp = str1[0]
            new_str = ""
            for j in str1:
                if j==tmp:
                    count +=1
                else:
                    new_str += (str(count) + str(tmp))
                    tmp = j
                    count = 1
            new_str += (str(count) + str(tmp))
            count = 0
            str1 = new_str

        return str1
