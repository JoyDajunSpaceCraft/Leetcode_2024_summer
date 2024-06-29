class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        result1 = self.robrange(nums, 1, len(nums)-1)
        result2 = self.robrange(nums, 0, len(nums)-2)
        return max(result1, result2)
    def robrange(self,  nums: List[int], start: int, end: int) -> int:
        if start==end:
            return nums[start]
        prev = nums[start]
        cur = max(prev, nums[start+1])

        for i in range(start+2, end+1):
            temp = cur
            cur = max(nums[i]+prev, cur)
            prev = temp
        return cur