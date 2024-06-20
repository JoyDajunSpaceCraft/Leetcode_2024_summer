
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for i in range(m+1)]
        for s in strs:
            zero = s.count("0")
            one = len(s) - zero
            for i in range(m, zero-1,-1):
                for j in range(n, one-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zero][j-one]+1)
        return dp[m][n]