class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        for idx, el in enumerate(arr):
            val = el
            for k in range(idx + 1, len(arr)):
                val ^= arr[k]
                if val == 0:
                    res += k - idx
        return res
        
