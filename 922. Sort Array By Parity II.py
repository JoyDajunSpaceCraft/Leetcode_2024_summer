class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        if len(nums)%2!=0:
            return []
        evenidx = 0
        oddidx=1
        result = [0]*len(nums)
        for i in range(len(nums)):
            # print(result)
            # print(nums[i]%2)
            if nums[i]%2!=0:# odd
                result[oddidx]=nums[i]
                oddidx+=2

            else:
                result[evenidx] = nums[i]
                evenidx+=2
        return result
