# https://programmercarl.com/0015.%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i]>0:
                return result
            
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            left = i+1
            right = len(nums)-1
            while left <right:
                sum_ = nums[i] + nums[left] + nums[right]

                if sum_>0:
                    right -=1
                elif sum_<0:
                    left +=1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left<right and  nums[right] ==nums[right-1]:
                        right-=1
                    while left<right and nums[left] == nums[left +1]:
                        left +=1
                    right-=1
                    left +=1
        return result
                
            