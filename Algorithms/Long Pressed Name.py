class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if name == typed:
            return True
        
        for c in name:
            try:
                index = typed.index(c)
                typed = typed[index+1:]   
            except:
                return False        
        return True
