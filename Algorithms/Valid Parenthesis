class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
       
        mapping_ch = {")": "(", "}": "{", "]": "["}
     
        for ch in s:
            if ch in mapping_ch:
                removed_ch = stack.pop() if stack else "k"
                if mapping_ch[ch] != removed_ch:
                    return False
            else:
                stack.append(ch)
               
        return not stack
