class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        c = 0

        result = 0

        while c < len(s):
            print(c)
            if c<=(len(s)-2) and ((s[c] == "I" and s[c+1] in "VX") or (s[c] == "X" and s[c+1] in "LC")or (s[c] == "C" and s[c+1]in "DM")):
                result+=(d[s[c+1]]-d[s[c]])
                c  += 2
            else:
                result+=d[s[c]]
                c += 1

        return result
