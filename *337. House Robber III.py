# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = self.traversal(root)
        return max(dp)
    def traversal(self, node):
        if not node:
            return (0,0)
        left = self.traversal(node.left)
        right =self.traversal(node.right)

        val_0 = max(left[0], left[1]) + max(right[0], right[1])

        val_1 = node.val + left[0] + right[0]

        return (val_0, val_1)
#     核心思想
# 对于每个节点，我们需要考虑两种情况：

# 不偷当前节点：此时最大金额是左右子节点的最大值之和。
# 偷当前节点：此时最大金额是当前节点的值加上不偷左右子节点的最大金额。
# 具体解释
# traversal函数
# 这个函数返回一个元组，表示两个值：

# val_0：不偷当前节点时的最大金额。
# val_1：偷当前节点时的最大金额。
# 动态规划状态转移
# 不偷当前节点：val_0 = max(left[0], left[1]) + max(right[0], right[1])

# left[0] 和 right[0] 表示不偷左/右子节点的最大金额。
# left[1] 和 right[1] 表示偷左/右子节点的最大金额。
# 我们不偷当前节点，所以我们可以选择偷或者不偷左右子节点，选择左右子节点的最大金额。
# 偷当前节点：val_1 = node.val + left[0] + right[0]

# 当前节点的值 node.val。
# 因为偷了当前节点，所以不能偷左右子节点，因此只能选择左右子节点不偷的情况 left[0] 和 right[0]。
# max(dp)解释
# 在 rob 函数中，我们最终返回的是根节点两种情况下的最大值，即 max(dp)，代表在根节点偷或者不偷的情况下取最大值。

# 例子解析
# 假设输入的树为 [3, 2, 3, null, 3, null, 1]，树的结构如下：

# markdown
# 复制代码
#     3
#    / \
#   2   3
#    \   \
#     3   1
# 对于最左边的叶节点 3，traversal(3) 返回 (0, 3)。
# 对于右边的叶节点 1，traversal(1) 返回 (0, 1)。
# 对于左子树根节点 2：
# 左子节点为 None，返回 (0, 0)。
# 右子节点为 3，traversal(3) 返回 (0, 3)。
# 因此 val_0 = max(0, 0) + max(0, 3) = 3，val_1 = 2 + 0 + 0 = 2，返回 (3, 2)。
# 对于右子树根节点 3：
# 左子节点为 None，返回 (0, 0)。
# 右子节点为 1，traversal(1) 返回 (0, 1)。
# 因此 val_0 = max(0, 0) + max(0, 1) = 1，val_1 = 3 + 0 + 0 = 3，返回 (1, 3)。
# 最后对于根节点 3：
# 左子树 traversal(2) 返回 (3, 2)。
# 右子树 traversal(3) 返回 (1, 3)。
# 因此 val_0 = max(3, 2) + max(1, 3) = 6，val_1 = 3 + 3 + 1 = 7，返回 (6, 7)。
# 最终结果为 max(6, 7) = 7，即最大金额为 7。






