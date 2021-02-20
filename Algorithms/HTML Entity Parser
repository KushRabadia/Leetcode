class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        dict1 = {"&quot;":'\"',"&apos;":"'","&amp;":"&","&gt;":">","&lt;":"<","&frasl;":"/"}
        d = dict1.keys()
        for i in d:
            while i in text:       
                text = text.replace(i,dict1[i])
        return text
