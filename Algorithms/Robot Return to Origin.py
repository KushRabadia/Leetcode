class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return (moves.count("L")==moves.count("R"))and(moves.count("D")==moves.count("U"))
