class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** N + 1) / 5 ** 0.5)
