class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        target_sum = total_sum // 2
        dp = [[False] * (target_sum + 1) for _ in range(len(nums) + 1)]
        # 初始化第一行（空子集可以得到和为0）
        for i in range(len(nums) + 1):
            dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, target_sum + 1):
                if j < nums[i - 1]:
                    # 当前数字大于目标和时，无法使用该数字
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 当前数字小于等于目标和时，可以选择使用或不使用该数字
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[len(nums)][target_sum]
    
#     第一个循环遍历所有物品。
# 第二个循环遍历所有可能的目标和 j。
# 不选择当前物品：if j < nums[i-1]，如果当前物品 nums[i-1] 重量超过当前目标和 j，则不能选择当前物品，dp[i][j] = dp[i-1][j]。
# 选择当前物品：else，我们可以选择或者不选择当前物品，dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]。这意味着如果前 i-1 个物品可以组成和为 j-nums[i-1] 的子集，或者前 i-1 个物品可以组成和为 j 的子集，那么前 i 个物品就可以组成和为 j 的子集