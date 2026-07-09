class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            seen=set()
            for num in i:
                if num!='.' and num in seen:
                    return False
                else: seen.add(num)            


        for col in range(len(board[0])):
            seen=set()
            for row in board:
                if row[col]!='.' and row[col] in seen:
                    return False
                else: seen.add(row[col])


        for box_col in range(0,9,3):
            for box_row in range(0,9,3):
                seen=set()
                for c in range(3):
                    for r in range(3):
                        if board[box_row+r][box_col+c] !='.' and board[box_row+r][box_col+c] in seen:
                            return False
                        else: 
                            seen.add(board[box_row+r][box_col+c])
        return True