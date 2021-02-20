class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        cnt = collections.Counter(arr)
        for k, v in sorted(cnt.items(), reverse=True):
            if k == v:
                return k
        return -1
