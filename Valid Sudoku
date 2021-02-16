class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        length = len(board)
        row_dict = defaultdict(set)
        column_dict = defaultdict(set)
        box_dict = defaultdict(set)
        
        for i in range(length):
            for j in range(length):
                num = board[i][j]
                if num == '.':
                    continue
                
                row_id = i
                column_id = j
                box_id = i // 3 * 3 + j // 3
                if num in row_dict[row_id] or num in column_dict[column_id] or num in box_dict[box_id]:
                    return False
                else:
                    row_dict[row_id].add(num)
                    column_dict[column_id].add(num)
                    box_dict[box_id].add(num)
                    
        return True
