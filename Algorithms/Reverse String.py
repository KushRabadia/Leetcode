class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        for i in range(int(len(s)/2)):
            first_char = s[i]
            s[i] = s[len(s) - i - 1]
            s[len(s) - i - 1] = first_char
