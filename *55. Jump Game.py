class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0  # 表示可以覆盖到的最远位置
        i = 0
        if len(nums) == 1: return True  # 如果数组长度为1，直接返回True

        # 当索引 i 小于等于当前能覆盖到的最远位置时
        while i <= cover:
            # 更新能覆盖到的最远位置
            cover = max(nums[i] + i, cover)
            # 如果能覆盖到或超过最后一个位置，返回True
            if cover >= len(nums) - 1: return True
            # 移动到下一个位置
            i += 1

        # 如果循环结束还没有返回True，说明无法到达最后一个位置
        return False
# 具体解释
# 变量初始化：

# cover = 0：初始时能覆盖到的最远位置是0。
# i = 0：从第一个位置开始。
# 特殊情况处理：

# 如果数组长度为1，直接返回True，因为已经在最后一个位置了。
# 主循环：

# while i <= cover:：只要当前索引 i 小于等于能覆盖到的最远位置 cover，就继续循环。
# 这里的条件 i <= cover 表示，只要当前索引 i 在能覆盖到的范围内，就继续检查能跳到的最远位置。
# 不是 while i <= len(nums): 的原因是，如果当前索引 i 超出了能覆盖到的最远位置 cover，就不可能再前进了，也就没必要继续检查了。
# 更新能覆盖到的最远位置：

# cover = max(nums[i] + i, cover)：更新当前能覆盖到的最远位置，选择当前位置 i 能跳到的最远位置和之前记录的最远位置的最大值。
# 提前返回：

# if cover >= len(nums) - 1: return True：如果能覆盖到或超过最后一个位置，直接返回 True。
# 循环结束后返回 False：

# 如果循环结束，还没有返回 True，说明无法到达最后一个位置，返回 False。
# 关于 = 号
# i <= cover 和 cover >= len(nums) - 1 中的等号：
# i <= cover：确保当前索引 i 在能覆盖到的范围内，并且等号确保在能覆盖到的最远位置也要检查。
# cover >= len(nums) - 1：等号确保当能正好跳到最后一个位置时，也能正确返回 True。