class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1

        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] += dp[j-coins[i]] # 内层循环遍历当前硬币能凑成的每个金额。对于每个金额 j，将 dp[j] 加上 dp[j - coins[i]] 的值，这表示用当前硬币 coins[i] 来凑成金额 j 的方法数。
                print(f"硬币 {coins[i]}, 金额 {j}, dp: {dp}")
        return dp[-1]