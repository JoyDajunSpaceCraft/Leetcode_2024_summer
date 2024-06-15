class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)# row
        n = len(obstacleGrid[0]) # col

        dp = [[0]*n for i in range(m)]
        if obstacleGrid[0][0] ==1 or obstacleGrid[-1][-1] == 1:
            return 0

        for i in range(m):
            if obstacleGrid[i][0]!=1:
                dp[i][0] =1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j]!=1:
                dp[0][j] =1
            else:
                break
        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col]!=1:

                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
                else:
                    continue
        return dp[-1][-1]