class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1): # 进行优化，从能装得下的背包开始计算，则不需要进行比较
                # 更新凑成金额 i 所需的最少硬币数量
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
