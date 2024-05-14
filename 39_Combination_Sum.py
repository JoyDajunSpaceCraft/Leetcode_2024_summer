class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cur = []
        res = []

        def dfs(i , total):
            if total==target:
                res.append(cur.copy())
                return
            if total > target:
                return 
            if i>=len(candidates):
                return 
            cur.append(candidates[i])
            dfs(i, total+candidates[i])
            cur.pop()
            dfs(i+1, total)
        dfs(0,0)
        return res

# dfs 函数的参数是 i 和 total：

# i：表示当前考虑的候选数的索引。
# total：表示当前组合的总和。
# 递归调用分析
# 1. dfs(i, total + candidates[i])
# 这行代码表示将当前的候选数 candidates[i] 加入到当前组合中，并且继续在当前索引 i 进行递归调用。具体步骤如下：

# 将 candidates[i] 加入到 cur 中（即当前组合）。
# 递归调用 dfs(i, total + candidates[i])，即继续尝试从 candidates[i] 开始选择下一个数。
# 递归返回后，将 cur 中最后一个数弹出（回溯）。
# 这一部分代码允许在组合中重复使用同一个数。例如，candidates = [2, 3, 6, 7] 和 target = 7 时，选择 2 后，可以继续选择 2，形成 [2, 2, 3]。

# 2. dfs(i + 1, total)
# 这行代码表示跳过当前的候选数 candidates[i]，从下一个索引 i + 1 开始进行递归调用。具体步骤如下：

# 不将 candidates[i] 加入到 cur 中。
# 递归调用 dfs(i + 1, total)，即尝试从 candidates 的下一个数开始选择。
# 这一部分代码确保我们尝试所有可能的组合。例如，跳过 2，直接选择 3 和 5，形成 [3, 5]。

# 例子分析
# 以第一个例子 candidates = [2, 3, 6, 7] 和 target = 7 为例，函数调用过程如下：

# 初始调用：dfs(0, 0)
# 选择 2，调用：dfs(0, 2)（总和 2）
# 选择 2，调用：dfs(0, 4)（总和 4）
# 选择 2，调用：dfs(0, 6)（总和 6）
# 选择 2，调用：dfs(0, 8)（超过目标，返回）
# 回溯，选择 3，调用：dfs(1, 6)（总和 6）
# 选择 3，调用：dfs(1, 9)（超过目标，返回）
# 回溯，选择 6，调用：dfs(2, 6)（总和 6）
# 回溯，选择 7，调用：dfs(3, 7)（总和 7，找到一个解）
# 通过这样递归调用和回溯，我们可以尝试所有可能的组合，从而找到所有满足条件的解。

# 总结
# dfs(i, total + candidates[i])：在当前索引 i 继续选择候选数，使得可以重复使用同一个数。
# dfs(i + 1, total)：跳过当前索引 i，从下一个索引开始选择候选数，确保尝试所有可能的组合。