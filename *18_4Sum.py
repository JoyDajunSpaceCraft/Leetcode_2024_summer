# https://programmercarl.com/0018.%E5%9B%9B%E6%95%B0%E4%B9%8B%E5%92%8C.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        result = []
        for i in range(len(nums)):
            
            if i> 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] > target and target > 0: #剪枝（可省）
                    break
                if j > i+1 and nums[j] == nums[j-1]: # 去重
                    continue
                left = j+1
                right = len(nums)-1
                while left< right:
                    sum_ = nums[j] + nums[i] + nums[left]+nums[right]
                    # print("nums[i]", nums[i])
                    # print("nums[j]", nums[j])
                    # print("nums[left]", nums[left])
                    # print("nums[right]", nums[right])
                    if sum_ < target:
                        left+=1
                    elif sum_ > target:
                        right-=1
                    else:
                        result.append([nums[i] ,nums[j], nums[left], nums[right]])
                
                        while left< right and nums[left] == nums[left+1]:
                            left+=1
                        while left< right and nums[right] == nums[right-1]:
                            right-=1
                        left+=1
                        right-=1 

        return result 