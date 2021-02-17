class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) >=1:
            prefix=strs[0]
            for s in strs[1:]:
                ph=''
                for i,j in zip(prefix,s):
                    print(i+" "+j)
                    if i==j:
                        ph+=i
                    else:
                        break
                if ph:
                    prefix=ph
                else:
                    return ''
            return prefix
                       
        else:
            return ""
