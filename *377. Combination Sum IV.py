class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [[0]*(target+1) for _ in nums]
        for i in range(len(nums)):
            dp[i][0] = 1
        for j in range(1, target+1):
            for i in range(len(nums)):
                if j-nums[i]>=0:
                    dp[i][j] = dp[i-1][j] + dp[-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]