class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        keyb = {'a': '2', 'b': '3', 'c': '3', 'd': '2', 'e': '1', 'f': '2', 'g': '2', 'h': '2', 'i': '1', 'j': '2', 'k': '2', 'l': '2', 'm': '3', 'n': '3', 'o': '1', 'p': '1', 'q': '1', 'r': '1', 's': '2', 't': '1', 'u': '1', 'v': '3', 'w': '1', 'x': '3', 'y': '1', 'z': '3'}

        for i in words:
            tmp = keyb[i[0].lower()]
            l = True
            j = 1
            while l and j < len(i):
                if keyb[i[j].lower()] != tmp:
                    l = False
                j+=1

            if l:
                result.append(i)

        return(result)
