class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        def s1(l1,l2):
            d = {}
            re = []
            for index, val in enumerate(l1):
                d[val] = index
            for index,val in enumerate(l2):
                if val in d: re.append([val, index + d[val]])
            min_index = min(x[1] for x in re )
            re =[ x[0] for x in re if x[1]== min_index]
            return re
        
        return s1(list1,list2)
