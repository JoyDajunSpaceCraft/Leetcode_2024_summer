class Solution:
    def jump(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 0
        
        # cur_distance = 0  # 当前覆盖最远距离下标
        # ans = 0  # 记录走的最大步数
        # next_distance = 0  # 下一步覆盖最远距离下标
        
        # for i in range(len(nums)):
        #     next_distance = max(nums[i] + i, next_distance)  # 更新下一步覆盖最远距离下标
        #     if i == cur_distance:  # 遇到当前覆盖最远距离下标
        #         ans += 1  # 需要走下一步
        #         cur_distance = next_distance  # 更新当前覆盖最远距离下标（相当于加油了）
        #         if next_distance >= len(nums) - 1:  # 当前覆盖最远距离达到数组末尾，不用再做ans++操作，直接结束
        #             break
        
        # return ans
        if len(nums)==1:
            return 0
        cur_distance = 0
        next_distance = 0
        ans = 0
        
        for i in range(len(nums)):
            next_distance = max(nums[i] + i, next_distance)
            if i==cur_distance:
                ans+=1
                cur_distance = next_distance
                if next_distance >= len(nums)-1:
                    break
        return ans


