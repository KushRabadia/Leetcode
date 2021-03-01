class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        e = re.search(r"^[-+]?\d+", str.lstrip())
        return max(min(int(e.group(0)), 2**31-1), -2**31) if e else 0
