class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        result = set()
        hash_map = { 'a' :".-",'b':"-...", 'c': "-.-.", 'd':"-..", 'e': ".", 'f': "..-.", 'g':"--.", 'h': "....", 'i': "..",    'j':  ".---",   'k':"-.-", 'l': ".-..", 'm':"--", 'n': "-.", 'o':"---", 'p':".--.", 'q': "--.-", 'r': ".-.", 's':"...", 't':"-", 'u': "..-", 'v': "...-", 'w': ".--", 'x':"-..-", 'y': "-.--", 'z':"--.."}
                    
            
        for word in words:
            new_str = ""
            for i in word:
                new_str = new_str+  hash_map[i]         
            result.add(new_str)
        
        return len(result)
