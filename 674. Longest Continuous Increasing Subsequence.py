class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        dp = [1]*len(nums)
        result = 1
        dp[0] = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1]+1
            result = max(result, dp[i])
        return result


