class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        size = len(nums)

        if size<=1:
            return size
        dp = [1]*size
        count = [1]*size
        max_c = 0
        for i in range(1, size):
            for j in range(i):

                if nums[i]>nums[j]:
                    if dp[j]+1>dp[i]:
                        dp[i] = dp[j]+1
                        count[i] = count[j]
                    elif dp[j]+1==dp[i]:
                        count[i] += count[j]
                if dp[i] > max_c:
                    max_c = dp[i]
                print("dp", dp)
                print("count", count)
        result = 0
        for i in range(size):
            if max_c == dp[i]:
                result += count[i]
        return result
               