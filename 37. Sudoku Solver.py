
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracking(board)
        
    def backtracking(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!=".": continue
                for k in range(1, 10):
                    if self.is_valid(i, j, k, board):
                        board[i][j] = str(k)
                        if self.backtracking(board): return True
                        board[i][j] = "."
                return False
        return True
    
    def is_valid(self, row, col,cur, board):
        cur = str(cur)
        print("cur in isvalid", cur)
        for i in range(9):
            if board[i][col] == cur:
                return False
        for j in range(9):
            if board[row][j] == cur:
                return False
        
        subrow = (row//3)*3
        subcol = (col//3)*3
        for i in range(subrow, subrow+3):
            for j in range(subcol, subcol+3):
                if board[i][j] == cur:
                    return False
        return True
