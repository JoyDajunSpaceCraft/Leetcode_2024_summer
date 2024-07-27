class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = nums[:]
        hash = dict()
        res.sort()
        for i, num in enumerate(res):
            if num not in hash.keys():
                hash[num] = i
        for i, num in enumerate(nums):
            res[i] = hash[num]
        return res

