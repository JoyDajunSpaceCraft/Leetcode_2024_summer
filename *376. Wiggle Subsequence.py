class Solution:
    
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        cur_diff = 0
        pre_diff = 0
        result = 1

        for i in range(len(nums)-1):
            cur_diff = nums[i+1] - nums[i]
            # pre_diff = nums[i] - nums[i-1]
            if( pre_diff<=0 and cur_diff>0 )or( pre_diff>=0 and cur_diff<0):
                result+=1
                pre_diff=cur_diff
        return result
        