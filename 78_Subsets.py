# 在 Python 中，列表是可变对象，直接传递列表的引用可能会导致意外的修改。通过 path[:] 传递的是 path 的一个副本，保证在 results 中存储的是当前 path 的快照，而不是对同一个 path 引用的多次存储。

# 具体来说，如果直接使用 results.append(path)，那么 results 中存储的是对同一个 path 列表的引用。当 path 发生变化时，results 中的所有对应元素也会跟着变化，这就导致了错误的结果。

# 通过 results.append(path[:])，在每次递归调用时都将 path 的当前状态保存下来，这样即使 path 在后续的递归调用中发生变化，也不会影响到 results 中已经保存的路径。

# 一个简单的例子可以更直观地说明这个问题：

# python
# 复制代码
# results = []
# path = [1, 2, 3]
# results.append(path)
# path.append(4)
# print(results)  # 输出 [[1, 2, 3, 4]]

# results = []
# path = [1, 2, 3]
# results.append(path[:])
# path.append(4)
# print(results)  # 输出 [[1, 2, 3]]
# 可以看到，直接 append(path) 会导致 results 中的内容随着 path 的变化而变化，而使用 append(path[:]) 可以避免这个问题。

# 在你的代码中，results.append(path[:]) 确保了在每次递归调用中，results 中保存的是当前 path 的副本，而不是引用，从而避免了路径被后续修改的影响。
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        self.backtracking(0, nums, results, [])
        return results

    def backtracking(self, index, nums, results, path):
        results.append(path[:])
        if len(path) > len(nums):
            return

        for i in range(index, len(nums)):
            path.append(nums[i])
            self.backtracking(i+1, nums, results, path)
            path.pop()
        

