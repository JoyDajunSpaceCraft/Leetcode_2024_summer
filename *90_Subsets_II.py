# https://programmercarl.com/0090.%E5%AD%90%E9%9B%86II.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
# 深入解释
# 让我们通过一个具体的示例来详细说明：

# 假设 nums = [1, 2, 2]，我们通过回溯法生成子集，同时跟踪 path 和 uset 的变化情况。

# 初始状态
# nums = [1, 2, 2]
# path = []
# result = [[]]
# 回溯过程详解
# 1. 第一次调用 backtracking 函数
# startIndex = 0
# 当前状态：path = []
# 遍历 nums 从 startIndex = 0 开始
# i = 0
# uset = set()

# path.append(nums[0])，即 path = [1]

# uset.add(nums[0])，即 uset = {1}

# 调用 backtracking(nums, 1, path, result)

# 结果更新：result = [[], [1]]
# 2. 第二次调用 backtracking 函数
# startIndex = 1
# 当前状态：path = [1]
# 遍历 nums 从 startIndex = 1 开始
# i = 1
# uset = set()

# path.append(nums[1])，即 path = [1, 2]

# uset.add(nums[1])，即 uset = {2}

# 调用 backtracking(nums, 2, path, result)

# 结果更新：result = [[], [1], [1, 2]]
# 3. 第三次调用 backtracking 函数
# startIndex = 2
# 当前状态：path = [1, 2]
# 遍历 nums 从 startIndex = 2 开始
# i = 2
# uset = set()

# path.append(nums[2])，即 path = [1, 2, 2]

# uset.add(nums[2])，即 uset = {2}

# 调用 backtracking(nums, 3, path, result)

# 结果更新：result = [[], [1], [1, 2], [1, 2, 2]]
# 回溯到第二次调用
# path.pop()，即 path = [1, 2]
# 当前状态：path = [1, 2]
# uset = {2}
# 结束遍历，因为 i 达到数组长度
# 回溯到第一次调用
# path.pop()，即 path = [1]
# 当前状态：path = [1]
# uset = {2}
# i = 2
# 跳过 nums[2]，因为 nums[2] 在当前的 uset 中
# 当前状态：path = [1]
# 结束遍历，因为 i 达到数组长度
# 回溯到初始调用
# path.pop()，即 path = []
# 当前状态：path = []
# uset = {1, 2}
# i = 1
# path.append(nums[1])，即 path = [2]

# uset.add(nums[1])，即 uset = {2}

# 调用 backtracking(nums, 2, path, result)

# 结果更新：result = [[], [1], [1, 2], [1, 2, 2], [2]]
# 第四次调用 backtracking 函数
# startIndex = 2
# 当前状态：path = [2]
# 遍历 nums 从 startIndex = 2 开始
# i = 2
# uset = set()

# path.append(nums[2])，即 path = [2, 2]

# uset.add(nums[2])，即 uset = {2}

# 调用 backtracking(nums, 3, path, result)

# 结果更新：result = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
# 回溯到第四次调用
# path.pop()，即 path = [2]
# 当前状态：path = [2]
# uset = {2}
# 结束遍历，因为 i 达到数组长度
# 回溯到初始调用
# path.pop()，即 path = []
# 当前状态：path = []
# uset = {2}
# 结论
# 通过这种方式，每次调用 backtracking 函数时，uset 都是独立的局部变量。它只用于当前函数调用范围内的去重操作，并不会影响其他递归调用中的 uset。这样，每一层递归调用都可以独立处理自己的去重逻辑，避免了重复子集的生成。
class Solution:
    def subsetsWithDup(self, nums):
        result = []
        path = []
        nums.sort()  # 去重需要排序
        self.backtracking(nums, 0, path, result)
        return result

    def backtracking(self, nums, startIndex, path, result):
        result.append(path[:])  # 收集子集
        uset = set()
        for i in range(startIndex, len(nums)):
            if nums[i] in uset:
                continue
            uset.add(nums[i])
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, result)
            path.pop()
