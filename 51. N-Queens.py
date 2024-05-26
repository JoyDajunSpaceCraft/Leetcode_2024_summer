# 使用 while i >= 0 and j >= 0: 而不是 while i > 0 and j > 0: 的原因是我们需要检查从当前皇后位置向左上对角线和右上对角线的所有位置，包括第0行和第0列。

# 如果我们改用 while i > 0 and j > 0:，我们将会遗漏第0行和第0列的位置检查，而这些位置也是可能放置皇后的地方。

# 具体来说：

# 示例
# 假设 n = 4，当前正在尝试将皇后放置在第2行第2列的位置：

# 左上对角线检查
# 当前皇后位置 (2, 2)
# i = 2 - 1 = 1
# j = 2 - 1 = 1
# 如果我们用 while i > 0 and j > 0:，检查开始时 i 和 j 都是 1，但它们会在第一次循环后变为 0，此时条件 i > 0 and j > 0 不再满足，因此不会检查第0行和第0列的 (0, 0) 位置。

# 但是如果我们用 while i >= 0 and j >= 0:，那么第0行和第0列的 (0, 0) 位置也会被检查到。


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chessboard = ["."*n for _ in range(n)]
        result = []
        self.backtracking(n, 0, chessboard, result)
        return result 

    def backtracking(self, n, row, chessboard, result):
        if row == n:
            result.append(chessboard[:])
            return
        
        for col in range(n):
            if self.is_valid(chessboard, row, col):

                chessboard[row] = chessboard[row][:col] + "Q" +chessboard[row][col+1:]
                self.backtracking(n, row+1, chessboard, result)
                chessboard[row] = chessboard[row][:col] + "." +chessboard[row][col+1:]


    def is_valid(self, chessboard, row, col):
        for i in range(row):
            if chessboard[i][col] =="Q":
                return False
        
        # judge diag
        i, j = row-1, col-1
        while i>=0 and j>=0: # here I am not add the =
            if chessboard[i][j] == "Q":
                return False
            i-=1
            j-=1

        
        i, j = row-1, col+1
        while i>=0 and j<len(chessboard):
            if chessboard[i][j] == "Q":
                return False
            i-=1
            j+=1

        return True
        
