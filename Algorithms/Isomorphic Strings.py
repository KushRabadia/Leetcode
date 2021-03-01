class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = True
        l = {}
        i = 0
        while d and i<len(s):
            if s[i] not in l and t[i] not in l.values():
                l[s[i]]=t[i]
            else:
                if s[i] in l:
                    if l[s[i]]!=t[i]:
                        d = False
                elif t[i] in l.values():
                    d = False
            i+=1

        return d
